import json
import os

os.makedirs('src/data', exist_ok=True)

with open('assets/photos_data.json', 'r', encoding='utf-8') as f:
    photos = json.load(f)

for p in photos:
    base = os.path.splitext(os.path.basename(p['src']))[0]
    p['webp'] = f"/assets/photos/{base}.webp"

with open('real_amenities.json', 'r', encoding='utf-8') as f:
    amenities_categories = json.load(f)

nearby_data = [
    {"title": "Beautiful Studio with a view to die for", "price": "₹23,600", "rating": "4.91", "img": "/assets/nearby/nearby_01.webp"},
    {"title": "NAQAB - 1bhk with private pool", "price": "₹42,218", "rating": "4.95", "img": "/assets/nearby/nearby_02.webp"},
    {"title": "Greentique Luxury Flat with plunge pool, Calangute", "price": "₹44,506", "rating": "4.94", "img": "/assets/nearby/nearby_03.webp"},
    {"title": "The Tropical Studio | 5 mins to Beach", "price": "₹22,824", "rating": "4.96", "img": "/assets/nearby/nearby_04.webp"},
    {"title": "Luxury Casa Bella 1BHK with plunge pool, Calangute", "price": "₹39,942", "rating": "4.95", "img": "/assets/nearby/nearby_05.webp"},
    {"title": "Kanso by Earthen Window | Jacuzzi | Terrace | Pool", "price": "₹45,648", "rating": "5.0", "img": "/assets/nearby/nearby_06.webp"},
    {"title": "Luxury Apt | Private Pool | 6 Mins from Beach", "price": "₹48,786", "rating": "4.93", "img": "/assets/nearby/nearby_07.webp"},
    {"title": "Serendipity Cottage - Calm Stay in Calangute-Baga.", "price": "₹22,824", "rating": "4.92", "img": "/assets/nearby/nearby_08.webp"}
]

categories = [
    {"key": "living1", "title": "Living room 1", "amenities": "Sofa · Air conditioning · Ceiling fan · TV"},
    {"key": "living2", "title": "Living room 2", "amenities": "Ceiling fan · Hot tub"},
    {"key": "kitchen", "title": "Full kitchen", "amenities": "Freezer · Fridge · Blender · Cooker · Cooking basics · Kettle · Microwave · Toaster · Wine glasses · Coffee · Crockery and cutlery"},
    {"key": "bedroom", "title": "Bedroom", "amenities": "Double bed · Air conditioning · Bed linen · Ceiling fan · Clothes storage · Cot · Hangers · Iron · Room-darkening blinds · Cleaning available during stay · Cleaning products · Long-term stays allowed · Private entrance · Wifi"},
    {"key": "bathroom", "title": "Full bathroom", "amenities": "Hot water · Shampoo · Hair dryer · Cleaning products"},
    {"key": "gym", "title": "Gym", "amenities": "Free weights · Exercise mat · Treadmill"},
    {"key": "exterior", "title": "Exterior", "amenities": ""},
    {"key": "pool", "title": "Pool", "amenities": "Pool"},
    {"key": "additional", "title": "Additional photos", "amenities": ""}
]

reviews = [
    {"name": "Amit", "tenure": "2 months on Airbnb", "when": "1 week ago", "text": "Very helpful and responsive team. Safe and peaceful stay. loved everything about the property.", "more": False},
    {"name": "Aheesh", "tenure": "3 years on Airbnb", "when": "2 weeks ago", "text": "We had a wonderful stay. The apartment was clean, comfortable, and exactly as shown in the photos. The host was very responsive and helpful throughout our stay. We would definitely recommend this place and would love to stay here again.", "more": True},
    {"name": "Samiksha", "tenure": "8 months on Airbnb", "when": "May 2026", "text": "the host nitish was really great help", "more": False},
    {"name": "Vedant", "tenure": "4 years on Airbnb", "when": "May 2026", "text": "We had an amazing stay at this property in Goa! The entire home was spotless and exceptionally well-maintained, making us feel comfortable from the moment we arrived. The cleanliness standards were truly impressive, with every corner of the house looking fresh and pristine…", "more": True},
    {"name": "Vaibhav S", "tenure": "2 years on Airbnb", "when": "May 2026", "text": "Great great experience living out there, can't expect more, will always look for it in the future and will recommend my friends too.", "more": False},
    {"name": "Mohd", "tenure": "1 year on Airbnb", "when": "May 2026", "text": "Great place. Exactly as described in the listing.", "more": False}
]

js_content = f"""// Auto-generated listing data for Romantic Jacuzzi 1BHK Candolim | Mirashya UG10
export const LISTING = {{
  id: "1599895892448055764",
  title: "Romantic Jacuzzi 1BHK Candolim | Mirashya UG10",
  type: "Entire serviced apartment in Candolim, India",
  specs: "3 guests · 1 bedroom · 1 bed · 1 bathroom",
  guestsMax: 3,
  bedrooms: 1,
  beds: 1,
  bathrooms: 1,
  rating: 4.95,
  reviewsCount: 19,
  guestFavourite: true,
  price: {{
    amount: "₹28,499",
    totalNumber: 28499,
    nights: 5,
    perNight: "₹5,700",
    checkin: "10/18/2026",
    checkout: "10/23/2026",
    dateRangeText: "18 Oct 2026 - 23 Oct 2026",
    freeCancelDate: "17 October"
  }},
  host: {{
    name: "Mirashya Homes",
    monogram: "MIRASHYA",
    yearsHosting: "2 years hosting",
    verified: true,
    stats: {{
      reviews: "1,463",
      rating: "4.68★",
      years: "2"
    }},
    facts: [
      "🎈 Born in the 80s",
      "🎓 Where I went to school: NICMAR GOA"
    ],
    coHosts: [
      {{ name: "Sharath", avatar: "S" }},
      {{ name: "Aman Dev Pahwa", avatar: "A" }},
      {{ name: "Maria Karen Priyanka", avatar: "M" }},
      {{ name: "Simran", avatar: "S" }},
      {{ name: "Pallavi", avatar: "P" }},
      {{ name: "Sanyukta", avatar: "S" }},
      {{ name: "Shruti", avatar: "S" }},
      {{ name: "Amisha", avatar: "A" }}
    ],
    details: [
      "Response rate: 100%",
      "Responds within an hour"
    ]
  }},
  description: `🌴 Plan Your Relaxing Holiday at Amor De Goa by Mirashya Homes! ✨ Stay in this cozy 1BHK in the heart of Candolim, featuring a private jacuzzi 🛁 for the perfect unwind. Enjoy high-speed WiFi 💻, Smart TV 📺, pet-friendly comfort 🐾, and stylish interiors. Just minutes from Candolim Beach 🏖️, popular cafés, restaurants, and nightlife 🍸, it's the ideal base whether you're here to relax, explore, or celebrate something special. Perfect for couples and small families looking for comfort, privacy, and a touch of romance. 🌴`,
  heroPhotoIndices: [3, 4, 12, 5, 28],
  categories: {json.dumps(categories, indent=2)},
  photos: {json.dumps(photos, indent=2)},
  reviews: {json.dumps(reviews, indent=2)},
  amenityCategories: {json.dumps(amenities_categories, indent=2)},
  nearby: {json.dumps(nearby_data, indent=2)}
}};
"""

with open('src/data/listingData.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated src/data/listingData.js with real 54 amenities successfully!")
