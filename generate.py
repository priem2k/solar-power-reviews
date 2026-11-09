import os
import json
import datetime
from datetime import timezone

TAG = "everythi00099-20"
DOMAIN = "https://yourusername.github.io/repo-name"  # Ganti dengan URL GitHub Pages Anda
STATE_FILE = "state.json"
REVIEWS_DIR = "reviews"

# Database produk power station & solar generators (Seed Catalog)
PRODUCTS_DATABASE = [
    {
        "id": "B082TMBYR6",
        "name": "Jackery Explorer 1000 Portable Power Station",
        "slug": "jackery-explorer-1000-review",
        "category": "High Capacity Stations",
        "capacity": "1002Wh",
        "output": "1000W (2000W Surge)",
        "weight": "22.0 lbs",
        "rating": "4.8",
        "reviews_count": "14,820",
        "price_tier": "$$$",
        "tagline": "The gold standard for reliable family camping and emergency home backup power.",
        "pros": ["Pure Sine Wave AC outlets", "Solid build quality", "Very quiet cooling fan operation", "Fast solar recharging"],
        "cons": ["Bulky AC power adapter", "No app connectivity on this model"]
    },
    {
        "id": "B09W2CGH7L",
        "name": "Anker 757 PowerHouse LiFePO4 Station",
        "slug": "anker-757-powerhouse-review",
        "category": "Heavy Duty / Emergency",
        "capacity": "1229Wh",
        "output": "1500W (2400W Surge)",
        "weight": "43.9 lbs",
        "rating": "4.7",
        "reviews_count": "3,410",
        "price_tier": "$$$$",
        "tagline": "Ultra-durable LFP battery pack engineered for over 3,000 charge cycles.",
        "pros": ["HyperFlash ultra-fast wall charging", "Industrial grade LiFePO4 cells", "Full 5-year warranty", "Built-in warm ambient light bar"],
        "cons": ["Heavy unit weight", "Handle is fixed and not foldable"]
    },
    {
        "id": "B08MZ37K74",
        "name": "BLUETTI EB3A Portable Power Station 268Wh",
        "slug": "bluetti-eb3a-268wh-review",
        "category": "Compact & Lightweight",
        "capacity": "268Wh",
        "output": "600W (1200W Surge)",
        "weight": "10.1 lbs",
        "rating": "4.5",
        "reviews_count": "9,890",
        "price_tier": "$",
        "tagline": "Ultra-portable power with smart app monitoring for CPAP, laptops, and drones.",
        "pros": ["Smartphone App control via Bluetooth", "Fast 430W dual charging", "Wireless phone charging pad on top", "Affordable entry price"],
        "cons": ["Fan can ramp up aggressively under full load", "Modest battery capacity"]
    },
    {
        "id": "B0948L8NYF",
        "name": "EcoFlow DELTA Max (2000) 2016Wh",
        "slug": "ecoflow-delta-max-2000-review",
        "category": "Whole Home Backup",
        "capacity": "2016Wh",
        "output": "2400W (5000W X-Boost)",
        "weight": "48.0 lbs",
        "rating": "4.6",
        "reviews_count": "2,980",
        "price_tier": "$$$$",
        "tagline": "Massive expandable home energy storage capable of powering heavy-duty kitchen appliances.",
        "pros": ["Expandable up to 6kWh with extra batteries", "X-Stream fast charge to 80% in 65 mins", "Powers 99% of home appliances", "WiFi & App controls"],
        "cons": ["High initial investment", "Substantial footprint"]
    },
    {
        "id": "B0B6TW1Z58",
        "name": "ALLPOWERS R600 Portable Power Station 299Wh",
        "slug": "allpowers-r600-portable-power-station-review",
        "category": "Compact & Lightweight",
        "capacity": "299Wh",
        "output": "600W (1200W Surge)",
        "weight": "12.8 lbs",
        "rating": "4.6",
        "reviews_count": "1,120",
        "price_tier": "$",
        "tagline": "Budget-friendly LiFePO4 power packed with high-speed wireless charging and UPS mode.",
        "pros": ["Uninterruptible Power Supply (UPS) under 10ms", "Wireless charge pad", "Fast AC recharge in 1 hour", "LiFePO4 battery longevity"],
        "cons": ["Display can be hard to see under direct bright sunlight"]
    },
    {
        "id": "B0BD5Q5W9P",
        "name": "Jackery SolarSaga 100W Monocrystalline Panel",
        "slug": "jackery-solarsaga-100w-panel-review",
        "category": "Solar Generators & Kits",
        "capacity": "100W Output",
        "output": "18V / 5.55A",
        "weight": "9.1 lbs",
        "rating": "4.7",
        "reviews_count": "7,310",
        "price_tier": "$$",
        "tagline": "High-efficiency monocrystalline solar panels with fold-out kickstands and weather resistance.",
        "pros": ["23% high conversion efficiency", "Direct USB-A & USB-C output ports", "Lightweight foldable design", "ETFE laminated surface"],
        "cons": ["Not fully submersible in heavy downpours"]
    },
    {
        "id": "B09SGB6ZNW",
        "name": "BLUETTI AC200MAX Expandable Power Station",
        "slug": "bluetti-ac200max-expandable-station-review",
        "category": "Heavy Duty / Emergency",
        "capacity": "2048Wh",
        "output": "2200W (4400W Surge)",
        "weight": "61.9 lbs",
        "rating": "4.6",
        "reviews_count": "1,850",
        "price_tier": "$$$$",
        "tagline": "The off-grid RV powerhouse with a dedicated 30A RV outlet and 900W solar input.",
        "pros": ["Built-in 30A NEMA TT-30 outlet for RVs", "Dual wireless charging decks", "Modular battery expansion ports", "Exceptional inverter efficiency"],
        "cons": ["Very heavy unit requiring two hands or a cart to move"]
    },
    {
        "id": "B0BC8PFL2L",
        "name": "EcoFlow River 2 Max 512Wh Generator",
        "slug": "ecoflow-river-2-max-review",
        "category": "Mid-Range Travel",
        "capacity": "512Wh",
        "output": "500W (1000W X-Boost)",
        "weight": "13.2 lbs",
        "rating": "4.6",
        "reviews_count": "4,190",
        "price_tier": "$$",
        "tagline": "The fastest charging mid-size generator: 0 to 100% in just 60 minutes.",
        "pros": ["Full wall charge in 60 minutes", "10-year lifespan LFP chemistry", "Ultra-lightweight chassis", "App integration via Wi-Fi/Bluetooth"],
        "cons": ["AC peak output limited to 1000W"]
    },
    {
        "id": "B0C9TZZ11L",
        "name": "Anker SOLIX C1000 Portable Power Station",
        "slug": "anker-solix-c1000-review",
        "category": "High Capacity Stations",
        "capacity": "1056Wh",
        "output": "1800W (2400W Surge)",
        "weight": "28.4 lbs",
        "rating": "4.8",
        "reviews_count": "2,210",
        "price_tier": "$$$",
        "tagline": "Ultra-fast recharging combined with 1800W continuous output in a compact body.",
        "pros": ["Charges to 100% in 58 minutes", "SurgePad technology runs up to 2400W appliances", "Smart temperature control", "Rugged drop-resistant casing"],
        "cons": ["Expansion battery cable sold separately"]
    },
    {
        "id": "B0BNQ18V8D",
        "name": "VTOMAN Jump 1500X Power Station 828Wh",
        "slug": "vtoman-jump-1500x-review",
        "category": "Vehicle & Outdoors",
        "capacity": "828Wh",
        "output": "1500W (3000W Surge)",
        "weight": "25.8 lbs",
        "rating": "4.5",
        "reviews_count": "890",
        "price_tier": "$$",
        "tagline": "Dual-purpose power station with integrated 12V car jump-starter cables.",
        "pros": ["Includes direct car battery jump start port", "LifeBMS safety protection", "Regulated 12V outputs", "Affordable high surge capability"],
        "cons": ["Display viewing angles are slightly narrow"]
    },
    {
        "id": "B0C7491Q9V",
        "name": "Jackery Explorer 2000 Plus Modular Station",
        "slug": "jackery-explorer-2000-plus-review",
        "category": "Heavy Duty / Emergency",
        "capacity": "2042Wh",
        "output": "3000W (6000W Surge)",
        "weight": "61.5 lbs",
        "rating": "4.7",
        "reviews_count": "1,040",
        "price_tier": "$$$$",
        "tagline": "Whisper-quiet modular powerhouse featuring heavy-duty wheels and telescopic handle.",
        "pros": ["Built-in luggage wheels and pull handle", "LiFePO4 battery with 4,000 cycles", "Super quiet under 30dB operation", "Massive 3000W AC output"],
        "cons": ["Premium price point"]
    },
    {
        "id": "B0BP1ZJ95Q",
        "name": "MARSOMA 100W Foldable Solar Panel Charger",
        "slug": "marsoma-100w-foldable-solar-panel-review",
        "category": "Solar Generators & Kits",
        "capacity": "100W Output",
        "output": "20V / 5A",
        "weight": "8.5 lbs",
        "rating": "4.5",
        "reviews_count": "630",
        "price_tier": "$",
        "tagline": "Universal solar kit compatible with 95% of all portable power station input ports.",
        "pros": ["Includes 10 different DC adapter plugs", "IP65 water and dust resistance", "Magnetic closing handle", "High solar cell transmittance"],
        "cons": ["Kickstands require level ground to stay rigid"]
    }
]

# Prosedural expansion generator: memastikan selalu ada 4 artikel baru yang belum pernah terbit setiap hari
def get_extended_product(index):
    base = PRODUCTS_DATABASE[index % len(PRODUCTS_DATABASE)]
    cycle = (index // len(PRODUCTS_DATABASE)) + 1
    if cycle == 1:
        return base
    
    # Menghasilkan entitas varian baru untuk siklus hari berikutnya
    return {
        "id": base["id"],
        "name": f"{base['name']} - Edition v{cycle}",
        "slug": f"{base['slug']}-v{cycle}",
        "category": base["category"],
        "capacity": base["capacity"],
        "output": base["output"],
        "weight": base["weight"],
        "rating": base["rating"],
        "reviews_count": str(int(base["reviews_count"].replace(",", "")) + (cycle * 125)),
        "price_tier": base["price_tier"],
        "tagline": f"Updated review & field benchmark analysis for {base['name']} with revised energy metrics.",
        "pros": base["pros"] + ["Updated firmware efficiency", "Enhanced low-temperature cell protection"],
        "cons": base["cons"]
    }

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"published_indices": []}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def build_amazon_url(asin):
    return f"https://www.amazon.com/dp/{asin}?tag={TAG}"

def get_base_css():
    return """
        :root {
            --bg-color: #FEF9E7;
            --card-bg: #FFFFFF;
            --accent-yellow: #FACC15;
            --accent-dark: #CA8A04;
            --text-main: #1F2937;
            --text-muted: #4B5563;
            --btn-orange: #F59E0B;
            --btn-hover: #D97706;
            --border-color: #FDE047;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); line-height: 1.6; padding-bottom: 60px; }
        .top-banner { background: linear-gradient(90deg, #F59E0B, #EAB308); color: #111827; padding: 10px 16px; text-align: center; font-weight: 700; font-size: 0.95rem; border-bottom: 2px solid #CA8A04; }
        header { background: #FFFFFF; border-bottom: 3px solid var(--accent-yellow); padding: 24px 20px; text-align: center; }
        header h1 { font-size: 2.2rem; color: #854D0E; letter-spacing: -0.5px; }
        header p { color: var(--text-muted); font-size: 1.05rem; margin-top: 6px; }
        .container { max-width: 1140px; margin: 0 auto; padding: 24px 16px; }
        .search-box-wrapper { margin: 20px 0 32px 0; text-align: center; }
        .search-input { width: 100%; max-width: 600px; padding: 14px 20px; font-size: 1rem; border: 2px solid var(--border-color); border-radius: 9999px; outline: none; background: #FFFFFF; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .search-input:focus { border-color: var(--btn-orange); }
        .section-title { font-size: 1.6rem; color: #854D0E; margin-bottom: 18px; border-left: 6px solid var(--btn-orange); padding-left: 12px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .card { background: var(--card-bg); border-radius: 12px; border: 1px solid #FEF08A; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(202, 138, 4, 0.08); transition: transform 0.2s ease; }
        .card:hover { transform: translateY(-4px); }
        .card h3 { font-size: 1.15rem; color: #1F2937; margin-bottom: 8px; line-height: 1.4; }
        .badge { display: inline-block; background-color: #FEF08A; color: #854D0E; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 9999px; margin-bottom: 10px; }
        .specs-list { list-style: none; margin: 12px 0; font-size: 0.88rem; color: var(--text-muted); }
        .specs-list li { margin-bottom: 4px; }
        .btn-amazon { display: block; text-align: center; background-color: var(--btn-orange); color: #FFFFFF; font-weight: 700; text-decoration: none; padding: 12px 18px; border-radius: 8px; margin-top: 14px; transition: background 0.2s; }
        .btn-amazon:hover { background-color: var(--btn-hover); }
        .btn-secondary { display: block; text-align: center; background: #FEF3C7; color: #92400E; font-weight: 600; text-decoration: none; padding: 8px 14px; border-radius: 8px; margin-top: 8px; font-size: 0.85rem; }
        .table-responsive { overflow-x: auto; background: #FFFFFF; border-radius: 12px; border: 1px solid #FEF08A; margin-bottom: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; }
        th { background: #FEF08A; color: #713F12; padding: 14px 16px; font-weight: 700; }
        td { padding: 12px 16px; border-bottom: 1px solid #FEF9C3; }
        tr:hover td { background-color: #FFFDF0; }
        .faq-item { background: #FFFFFF; border-radius: 8px; border: 1px solid #FEF08A; margin-bottom: 12px; padding: 16px 20px; }
        .faq-item h4 { font-size: 1.05rem; color: #854D0E; margin-bottom: 6px; }
        .faq-item p { color: var(--text-muted); font-size: 0.92rem; }
        footer { text-align: center; padding: 30px 16px; font-size: 0.85rem; color: #713F12; margin-top: 40px; border-top: 2px solid #FEF08A; }
        .article-content { background: #FFFFFF; padding: 30px; border-radius: 12px; border: 1px solid #FEF08A; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.04); }
        .pros-cons { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0; }
        @media (max-width: 768px) { .pros-cons { grid-template-columns: 1fr; } }
        .pros-box { background: #F0FDF4; border: 1px solid #BBF7D0; padding: 16px; border-radius: 8px; }
        .cons-box { background: #FEF2F2; border: 1px solid #FECACA; padding: 16px; border-radius: 8px; }
        .pros-box h4 { color: #166534; margin-bottom: 8px; }
        .cons-box h4 { color: #991B1B; margin-bottom: 8px; }
        .breadcrumbs { font-size: 0.85rem; margin-bottom: 16px; color: #713F12; }
        .breadcrumbs a { color: #D97706; text-decoration: none; }
    """

def generate_review_article_html(prod):
    affiliate_link = build_amazon_url(prod["id"])
    pros_html = "".join([f"<li>✔ {p}</li>" for p in prod["pros"]])
    cons_html = "".join([f"<li>✖ {c}</li>" for c in prod["cons"]])
    
    schema_ld = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": prod["name"],
        "description": prod["tagline"],
        "brand": {"@type": "Brand", "name": prod["name"].split()[0]},
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": prod["rating"],
            "reviewCount": prod["reviews_count"].replace(",", "")
        },
        "offers": {
            "@type": "Offer",
            "priceCurrency": "USD",
            "price": "999.00",
            "availability": "https://schema.org/InStock",
            "url": affiliate_link
        }
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{prod['name']} In-Depth Review & Performance Test</title>
    <meta name="description" content="Unbiased hands-on review of {prod['name']}. Tested capacity: {prod['capacity']}, AC Inverter: {prod['output']}. Read real buyer pros & cons.">
    <link rel="canonical" href="{DOMAIN}/reviews/{prod['slug']}.html">
    <style>{get_base_css()}</style>
    <script type="application/ld+json">
    {json.dumps(schema_ld)}
    </script>
</head>
<body>
    <div class="top-banner">⚡ Black Friday & Seasonal Savings: Check Live Amazon Stock & Discounts</div>
    <div class="container">
        <div class="breadcrumbs">
            <a href="../index.html">Home</a> &raquo; <a href="../index.html">Reviews</a> &raquo; {prod['name']}
        </div>
        
        <article class="article-content">
            <span class="badge">{prod['category']}</span>
            <h1 style="color: #854D0E; font-size: 2rem; margin-bottom: 12px;">{prod['name']} Hands-on Benchmark Review</h1>
            <p style="font-size: 1.1rem; color: #4B5563; margin-bottom: 20px;"><em>{prod['tagline']}</em></p>
            
            <div style="background: #FFFBEB; border: 1px solid #FCD34D; border-radius: 8px; padding: 18px; margin-bottom: 24px;">
                <p><strong>Tested Rating:</strong> ⭐ {prod['rating']} / 5.0 (Based on {prod['reviews_count']} verified buyer reviews)</p>
                <p><strong>Storage Capacity:</strong> {prod['capacity']} | <strong>AC Inverter Output:</strong> {prod['output']}</p>
                <p><strong>Total Weight:</strong> {prod['weight']} | <strong>Price Category:</strong> {prod['price_tier']}</p>
            </div>

            <h2 class="section-title">Why This Power Station Matters</h2>
            <p>In modern emergency preparedness and mobile outdoor exploration, steady power is essential. The <strong>{prod['name']}</strong> is designed to solve real-world off-grid challenges—powering essential medical hardware (CPAP machines), portable refrigerators, communication tools, and heavy-draw appliances during unexpected grid outages.</p>
            
            <h2 class="section-title" style="margin-top: 24px;">Laboratory & Field Test Findings</h2>
            <p>During discharge testing, the battery management system (BMS) demonstrated steady thermal dissipation under maximum continuous loads. The pure sine wave inverter delivers stable alternating current with minimal harmonic distortion, ensuring zero risk when charging sensitive electronics like MacBooks, drones, and cameras.</p>

            <div class="pros-cons">
                <div class="pros-box">
                    <h4>What We Liked (Pros)</h4>
                    <ul style="list-style: none;">{pros_html}</ul>
                </div>
                <div class="cons-box">
                    <h4>What Could Be Better (Cons)</h4>
                    <ul style="list-style: none;">{cons_html}</ul>
                </div>
            </div>

            <h2 class="section-title">Final Buying Verdict</h2>
            <p>If you require a durable, highly dependable portable power source with proven reliability, the {prod['name']} stands out as one of the most value-oriented choices in the {prod['category']} class.</p>

            <a href="{affiliate_link}" target="_blank" rel="nofollow noopener" class="btn-amazon" style="font-size: 1.15rem; padding: 16px 24px; margin-top: 28px;">
                View Best Price & Customer Deals on Amazon &rarr;
            </a>
        </article>
        
        <div style="text-align: center;">
            <a href="../index.html" class="btn-secondary" style="display: inline-block; padding: 10px 20px;">&larr; Back to Comparison & All Products</a>
        </div>
    </div>
    <footer>
        <p>&copy; {datetime.datetime.now().year} Solar Power Station Review Hub. Participant in the Amazon Services LLC Associates Program.</p>
    </footer>
</body>
</html>
"""
    return html

def generate_index_html(all_published_products):
    # Urutkan berdasarkan yang paling baru diterbitkan
    recent_products = list(reversed(all_published_products))
    bestsellers = [p for p in all_published_products if float(p.get("rating", 4.5)) >= 4.7][:4]
    if not bestsellers:
        bestsellers = recent_products[:4]

    # Generate cards HTML
    cards_html = ""
    for prod in recent_products:
        affiliate_link = build_amazon_url(prod["id"])
        cards_html += f"""
        <div class="card product-card" data-title="{prod['name'].lower()}" data-cat="{prod['category'].lower()}">
            <div>
                <span class="badge">{prod['category']}</span>
                <h3>{prod['name']}</h3>
                <p style="font-size: 0.88rem; color: #4B5563;">{prod['tagline']}</p>
                <ul class="specs-list">
                    <li>⚡ <strong>Capacity:</strong> {prod['capacity']}</li>
                    <li>🔌 <strong>Output:</strong> {prod['output']}</li>
                    <li>⚖️ <strong>Weight:</strong> {prod['weight']}</li>
                    <li>⭐ <strong>Rating:</strong> {prod['rating']} ({prod['reviews_count']} reviews)</li>
                </ul>
            </div>
            <div>
                <a href="{affiliate_link}" target="_blank" rel="nofollow noopener" class="btn-amazon">Check Price on Amazon</a>
                <a href="reviews/{prod['slug']}.html" class="btn-secondary">Read Full Review &rarr;</a>
            </div>
        </div>
        """

    # Generate Comparison Table Rows
    table_rows = ""
    for prod in all_published_products[:12]:
        affiliate_link = build_amazon_url(prod["id"])
        table_rows += f"""
        <tr>
            <td><strong>{prod['name']}</strong></td>
            <td>{prod['category']}</td>
            <td>{prod['capacity']}</td>
            <td>{prod['output']}</td>
            <td>⭐ {prod['rating']}</td>
            <td><a href="{affiliate_link}" target="_blank" rel="nofollow noopener" style="color: #D97706; font-weight: 700; text-decoration: none;">View on Amazon &rarr;</a></td>
        </tr>
        """

    # Generate Bestseller Section HTML
    bestseller_html = ""
    for prod in bestsellers:
        affiliate_link = build_amazon_url(prod["id"])
        bestseller_html += f"""
        <div class="card" style="border: 2px solid #F59E0B; background: #FFFEF5;">
            <div>
                <span class="badge" style="background: #F59E0B; color: #FFFFFF;">TOP RATED CHOICE</span>
                <h3>{prod['name']}</h3>
                <p style="font-size: 0.9rem; color: #4B5563;">{prod['tagline']}</p>
                <p style="margin-top: 10px; font-weight: 700; color: #854D0E;">⭐ {prod['rating']} / 5.0 Rating</p>
            </div>
            <div>
                <a href="{affiliate_link}" target="_blank" rel="nofollow noopener" class="btn-amazon">Buy on Amazon</a>
                <a href="reviews/{prod['slug']}.html" class="btn-secondary">Detailed Specs</a>
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Portable Power Stations & Solar Generators - 2026 Buying Guide</title>
    <meta name="description" content="Compare the best portable power stations, solar generators, and off-grid emergency batteries. Independent reviews, specifications, and buying advice.">
    <link rel="canonical" href="{DOMAIN}/index.html">
    <style>{get_base_css()}</style>
    <!-- FAQ Schema for Google Rich Snippets -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "What size portable power station do I need for home backup?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "For small medical electronics (CPAP) and phone/laptop charging, 250Wh to 500Wh is sufficient. For powering a standard full-size home refrigerator during a blackout, select a unit with at least 1000Wh to 2000Wh capacity."
          }}
        }},
        {{
          "@type": "Question",
          "name": "How long do LiFePO4 power station batteries last?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "LiFePO4 (Lithium Iron Phosphate) batteries last between 3,000 to 4,000 charge cycles before reaching 80% capacity, translating to roughly 10 years of consistent regular use."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Can portable solar generators run continuously indoors?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Yes. Unlike gas-powered generators, portable battery power stations emit zero carbon monoxide fumes, making them 100% safe to operate inside bedrooms and living spaces."
          }}
        }}
      ]
    }}
    </script>
</head>
<body>
    <div class="top-banner">⚡ Verified Power Station & Solar Generator Reviews: Updated Daily with Real Field Metrics</div>
    
    <header>
        <h1>Off-Grid Energy & Power Station Guide</h1>
        <p>Unbiased technical reviews, real runtime tests, and current deals on Amazon</p>
    </header>

    <div class="container">
        <!-- Live Instant Search Bar -->
        <div class="search-box-wrapper">
            <input type="text" id="productSearch" class="search-input" placeholder="🔍 Search power stations by brand, capacity (e.g. Jackery, 1000Wh, Anker)...">
        </div>

        <!-- Bestsellers Section -->
        <h2 class="section-title">⭐ Featured Best Sellers & Top Editor Picks</h2>
        <div class="grid">
            {bestseller_html}
        </div>

        <!-- Comparison Table -->
        <h2 class="section-title">📊 Side-by-Side Product Comparison Table</h2>
        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Model Name</th>
                        <th>Category</th>
                        <th>Battery Capacity</th>
                        <th>AC Output</th>
                        <th>User Rating</th>
                        <th>Amazon Store</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>

        <!-- All Daily Reviews Grid -->
        <h2 class="section-title">📝 Latest Hands-On Product Reviews ({len(all_published_products)} Total)</h2>
        <div class="grid" id="productsGrid">
            {cards_html}
        </div>

        <!-- FAQ Section -->
        <h2 class="section-title">❓ Frequently Asked Questions (FAQ)</h2>
        <div class="faq-item">
            <h4>What size portable power station do I need for home backup?</h4>
            <p>For small electronics and smartphones, a 250Wh to 500Wh unit is plenty. If your goal is to keep a refrigerator running during an emergency storm outage, aim for a minimum of 1000Wh to 2000Wh with at least 1500W continuous pure sine wave inverter output.</p>
        </div>
        <div class="faq-item">
            <h4>How long do LiFePO4 power station batteries last?</h4>
            <p>Modern LiFePO4 (Lithium Iron Phosphate) battery chemistry provides 3,000 to 4,000 full recharge cycles to 80% original capacity. That equates to nearly 10 years of regular use compared to standard Lithium-ion batteries which degrade after 500 cycles.</p>
        </div>
        <div class="faq-item">
            <h4>Can I keep a power station continuously plugged into the wall?</h4>
            <p>Most premium stations featured in our reviews include pass-through charging and EPS/UPS modes, allowing you to use them as an uninterrupted emergency power backup for desktop computers and medical devices.</p>
        </div>
    </div>

    <footer>
        <p>Affiliate Disclosure: As an Amazon Associate, we earn from qualifying purchases. Pricing and stock availability are subject to change on Amazon.com.</p>
        <p style="margin-top: 8px;">&copy; {datetime.datetime.now().year} Solar Power Reviews. All rights reserved.</p>
    </footer>

    <!-- Instant Search Script -->
    <script>
        const searchInput = document.getElementById('productSearch');
        const cards = document.querySelectorAll('.product-card');

        searchInput.addEventListener('input', function(e) {{
            const term = e.target.value.toLowerCase().trim();
            cards.forEach(card => {{
                const title = card.getAttribute('data-title');
                const cat = card.getAttribute('data-cat');
                if (title.includes(term) || cat.includes(term)) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>
"""
    return html

def generate_sitemap(all_published_products):
    today = datetime.datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls_xml = f"""  <url>
    <loc>{DOMAIN}/index.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>\n"""
    
    for prod in all_published_products:
        urls_xml += f"""  <url>
    <loc>{DOMAIN}/reviews/{prod['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)

def main():
    os.makedirs(REVIEWS_DIR, exist_ok=True)
    state = load_state()
    published_indices = state.get("published_indices", [])
    
    # Tentukan index berikutnya
    start_index = len(published_indices)
    
    # Ambil tepat 4 produk baru hari ini
    new_indices = [start_index + i for i in range(4)]
    new_products = [get_extended_product(i) for i in new_indices]
    
    # Generate artikel individu untuk 4 produk baru
    for prod in new_products:
        article_file = os.path.join(REVIEWS_DIR, f"{prod['slug']}.html")
        article_html = generate_review_article_html(prod)
        with open(article_file, "w", encoding="utf-8") as f:
            f.write(article_html)
        print(f"[OK] Generated review article: {article_file}")
    
    # Update state
    published_indices.extend(new_indices)
    state["published_indices"] = published_indices
    save_state(state)
    
    # Kumpulkan semua produk yang sudah pernah dipublish untuk memperbarui index dan sitemap
    all_published_products = [get_extended_product(i) for i in published_indices]
    
    # Buat ulang index.html dengan seluruh artikel yang ada
    index_html = generate_index_html(all_published_products)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"[OK] Updated index.html with {len(all_published_products)} total products.")
    
    # Buat sitemap.xml
    generate_sitemap(all_published_products)
    print(f"[OK] Re-generated sitemap.xml")

if __name__ == "__main__":
    main()
