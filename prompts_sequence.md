# Sequence of AI-Assisted Development Prompts

This document records the sequence of prompts and AI workflows used during the development of the high-fidelity Airbnb listing clone and production-scale vacation-rental architecture for the Playpower Labs assignment.

---

## Prompt 1: Discovery, Requirement Ingestion & Reference Verification
```text
Check the reference URL https://airbnb-clone-umber-two.vercel.app/ and read the Playpower Labs Assignment_ Airbnb-Clone App.md. Replace the placeholder images in airbnb-clone-source (1).html with the real listing images from the reference site. Check all required elements between the reference and our site to ensure exact pixel-perfect visual and behavioral parity.
```
**AI Action & Engineering Response:**
- Investigated the Vercel security challenge blocking headless automated fetches.
- Extracted reference screenshots (`ref_image1.png`, `ref_image2.png`, `ref_image3.png`) embedded in the assignment specification.
- Tracked the authentic Airbnb listing (`rooms/1599895892448055764` - *Romantic Jacuzzi 1BHK Candolim | Mirashya UG10*).
- Downloaded all 43 high-definition property photos categorized into the 9 exact room categories and 8 nearby stay photos.

---

## Prompt 2: Architecture Evolution to React & WebP Optimization
```text
There is a change in plan: I want the clone in React. We need to use components properly, convert all images to WebP for lightweight performance, configure MCP in .agents/mcp_config.json as needed, and update skills too.
```
**AI Action & Engineering Response:**
- Converted all 43 listing photos and 8 nearby stay photos from JPEG to modern `.webp` format (reducing payload by 26.1% from 7.82MB to 5.78MB).
- Initialized a modular React 19 + Vite project structure with Domain-Driven Design (DDD).
- Created atomic and composite components:
  - `Header`, `SearchBar`, `ListingHeader` (Share & Wishlist toggle)
  - `GalleryGrid` (5-tile hero grid with hover zoom matching `ref_image1.png`)
  - `StickyTabs` (IntersectionObserver active tab spy and quick reserve)
  - `Overview`, `Highlights`, `Description` (expandable with gradient fade)
  - `SleepingArrangements` (Bedroom & Living room cards with WebP photos)
  - `Amenities` & `AmenitiesModal` (54 real categorized amenities from Airbnb)
  - `CalendarSection` (dual-month stay picker for Oct/Nov 2026)
  - `Reviews` (4.95 rating hero with laurel leaves, progress bars, category pills, review cards)
  - `LocationMap` (styled Candolim map with pin and controls)
  - `HostSection` (Mirashya Homes profile, 1,463 reviews, 8 co-hosts, details)
  - `ThingsToKnow` (Cancellation, house rules, safety)
  - `NearbyStays` (paged sliding carousel with 8 stays)
  - `BookingCard` (sticky widget with ₹28,499 for 5 nights, dates, guests, free cancellation)
  - `PhotoTourModal` (full-screen 43-photo gallery matching `ref_image2.png`)
  - `LightboxModal` (single-photo viewer with keyboard `←`/`→` navigation matching `ref_image3.png`)
  - `Toast` (notification toast system)

---

## Prompt 3: FAANG Principal Engineering Audit & Production Architecture
```text
Are you sure? We need an in-depth implementation plan, push innovation, think outside the box, evaluate multiple approaches, best folder architecture, compatibility on sub-services, real-time test cases, and plan things like a FAANG engineer with architecture diagrams.
```
**AI Action & Engineering Response:**
- Enforced the **SWAT Security & Quality Matrix** (Security, Write-Safety, Availability, Threat).
- Performed trade-off analysis comparing Monolithic Static HTML, Next.js 15 SSR, and Enterprise React 19 + Vite.
- Implemented real-time test suite (`src/tests/listing.test.js`) covering listing data, hero tile mapping, 43 WebP photo verification, 8 nearby stays, 5-night pricing engine, and 54 amenities.
- Generated high-resolution production architecture diagram (`architecture_diagram.svg` and `architecture_diagram.png`) covering:
  - Global Anycast CDN (Cloudflare) with Edge Image Optimization (WebP/AVIF)
  - Envoy API Gateway with GraphQL Federation (Apollo Router)
  - Core Microservices on Multi-Region Kubernetes (Search, Listing, Booking Saga, Pricing, Reviews, Host, Messaging, Recommendations)
  - Distributed Caching (Redis Enterprise Cluster with Redlock algorithm)
  - Event Streaming (Apache Kafka with Debezium CDC)
  - Persistent Storage (OpenSearch Geospatial H3 Cluster, PostgreSQL Citus Sharding, Cloudflare R2 / S3)
  - DevOps, Observability (OpenTelemetry, Prometheus, Grafana), and Disaster Recovery.
- Wrote full architectural specification document (`architecture_design.md`).
- Authored custom AI agent skill `.agents/skills/expert_airbnb_cloning/SKILL.md`.
- Verified 100% build and test pass (`npm run build` and `node --test`).
- Captured visual screenshots of all 3 views confirming pixel-perfect parity with reference.
