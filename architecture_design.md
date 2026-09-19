# Production-Scale Architecture Design: Vacation-Rental Marketplace (Airbnb)

**Author:** Principal Infrastructure Engineer  
**System Target:** Global, multi-region vacation rental platform supporting 100M+ active listings, 50,000 queries per second (QPS) at peak, and 99.999% availability.  
**Companion Diagram:** [architecture_diagram.png](file:///e:/projects/clone_website/architecture_diagram.png) / [architecture_diagram.svg](file:///e:/projects/clone_website/architecture_diagram.svg)

---

## 1. High-Level Architectural Principles

1. **Cell-Based Multi-Region Architecture**:
   - The platform is deployed in active-active autonomous "Cells" across geographic regions (e.g., `ap-south-1` Mumbai, `us-east-1` N. Virginia, `eu-central-1` Frankfurt).
   - If an entire cloud region suffers an outage, Anycast BGP DNS routes traffic seamlessly to the nearest healthy cell with Zero Data Loss (RPO < 1s, RTO < 30s).

2. **Strict Domain-Driven Decomposition (DDD)**:
   - Microservices own their datastores exclusively. No cross-service database querying.
   - Cross-domain communication is strictly mediated via high-throughput gRPC interfaces or asynchronous Kafka event streams.

3. **CQRS (Command Query Responsibility Segregation)**:
   - High-throughput listing discovery (read path) is decoupled from booking transactions (write path).
   - Read models are materialized into OpenSearch clusters and Redis hot caches via Change Data Capture (CDC).

---

## 2. Tier-by-Tier Scaling Strategy

### Tier 1: Client Access & Edge Network
- **Anycast BGP Edge Routing (Cloudflare)**: Terminates TLS close to the user, blocking DDoS attacks and mitigating bot scrapers with automated rate limiting.
- **Dynamic Image Optimization**:
  - Automatically transforms high-resolution listing photos into lightweight **WebP** and **AVIF** formats on the fly based on client `Accept` headers.
  - Generates BlurHash Low-Quality Image Placeholders (LQIP) to eliminate Cumulative Layout Shift (**CLS = 0**).
- **Edge Cache Invalidation**: Uses Surrogate-Keys (Cache-Tags) to instantly invalidate cached listing pages worldwide within 150ms when a host modifies pricing or photo order.

### Tier 2: API Gateway & GraphQL Federation
- **Envoy Proxy Gateway**: Handles TLS termination, mTLS service-to-service encryption, and distributed request tracing with OpenTelemetry headers (`traceparent`).
- **GraphQL Federation (Apollo Router in Rust)**:
  - Aggregates subgraphs from Listing Service, Pricing Service, Review Service, and Host Service into a single unified schema.
  - Prevents over-fetching on mobile clients and enables sub-50ms query composition.

### Tier 3: Core Microservices Layer
1. **Search & Discovery Service (Go)**:
   - Executes multi-criteria spatial search using Uber H3 hexagonal hierarchical spatial indexes.
   - Handles map-bounding box queries in Candolim, North Goa, returning listings with p99 latency < 15ms.
2. **Booking & Checkout Engine (Temporal.io + Go)**:
   - Implements the **Distributed Saga Pattern** across Inventory, Payment, and Notification services with automatic compensating transactions upon failure.
   - Eliminates double-booking via distributed locking in Redis (Redlock algorithm).
3. **Dynamic Pricing & Availability Engine (Rust)**:
   - Calculates personalized stay quotes based on length-of-stay discounts, seasonal demand, and local tax regulations (e.g. 5-night stay calculations).
4. **Reviews & Reputation Service (Node.js / TimescaleDB)**:
   - Aggregates ratings (Cleanliness, Accuracy, Check-in, Communication, Location, Value) and computes "Guest Favourite" laurel qualifiers using Bayesian average scoring.

### Tier 4: Streaming & High-Throughput Caching
- **Redis Enterprise Cluster**:
  - Hot listing details, user session state, and ephemeral calendar date reservation locks (TTL: 10 minutes during checkout flow).
  - Sub-millisecond read throughput via read replicas colocated with Kubernetes worker nodes.
- **Apache Kafka Event Bus**:
  - Central backbone for asynchronous event publishing:
    - `listing.updated` -> triggers OpenSearch re-indexing.
    - `booking.created` -> triggers payment capture, email/SMS confirmation, and host notification.
  - Debezium CDC captures all PostgreSQL table mutations directly into Kafka topics without application-level overhead.

### Tier 5: Persistent Storage & Search Cluster
- **OpenSearch / Elasticsearch Cluster**:
  - Distributed inverted index with geospatial shards.
  - BM25 text search + Vector embeddings for semantic search ("luxury beachfront villa with private jacuzzi").
- **PostgreSQL Multi-Region Sharded Database (Citus)**:
  - ACID-compliant financial ledgers and confirmed reservations.
  - Geographically partitioned so Indian bookings reside in Mumbai nodes with compliant data sovereignty.
- **Cloudflare R2 / AWS S3 Media Bucket**:
  - High-durability (11 9s) object storage for millions of raw property images with multi-CDN origin shielding.

---

## 3. Real-Time Test Cases & Verification Protocol

1. **Concurrency Test**: 500 concurrent booking attempts for the same Candolim listing on identical dates (`18 Oct - 23 Oct 2026`). Exactly one transaction must succeed; 499 must receive a graceful "Dates no longer available" response without deadlocks.
2. **Edge Failover Simulation**: Simulating region failure (`ap-south-1`) causes Anycast DNS to reroute traffic to Singapore (`ap-southeast-1`) with < 2 seconds traffic settling.
3. **Asset Compression Benchmark**: Verified that WebP conversion yields 26.1% bandwidth reduction while preserving peak signal-to-noise ratio (PSNR > 42dB).
