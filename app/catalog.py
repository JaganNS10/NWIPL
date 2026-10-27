"""Page content that is not edited from the admin. Image paths are relative to static/."""

CLIENTS = [
    ("Akshaya", "akshayalogo.jpg"), ("Bharatiya Fashion", "bharatiyafashion.webp"),
    ("BSCPL", "bscpl.webp"), ("Casagrand", "Casagrandlogo.webp"),
    ("Etica Developers", "eticadevelopers.jpg"), ("J Stilo", "j-stilologo.jpg"),
    ("Navins", "navins.png"), ("NXG Homes", "nxghomes.jpg"), ("RWD", "RWD-logo.png"),
    ("Lifestyle", "lifestyle-new.png"), ("Babyshop", "babyshop-new.png"), ("HTL", "htl-logo.png"),
    ("S&S", "s&s.png"), ("Shriram", "shriramproperities.jpg"), ("Sycon", "syconconstruction.png"),
    ("TVH", "tvh.png"), ("Innovative", "Innovative.png"), ("Home Centre", "homecentre-new.png"),
    ("Centrepoint", "centrepoint-new.png"), ("New Century", "NewCentury.png"),
    ("Vodafone", "vodafone.jpg"), ("bbcl", "bbcl.webp"),
]

HERO_SLIDES = [
    "images/slideshow/featured-compressed-46.jpg",
    "images/slideshow/wooden-furniture-1.jpg",
    "images/slideshow/complement-light-oak-with-mid-century-furniture.jpg",
]

SHOP_TILES = [
    ("Luxury wooden interior furniture", "shop/Interiordesign.jpg", "products"),
    ("Modern dining room with wooden furniture", "shop/mock-up-poster-modern-dining-room-interior-design-with-white-empty-wall.jpg", "products"),
    ("Living Room", "shop/green-sofa-white-living-room-with-blank-table-mockup.jpg", "products"),
    ("Chef Kitchen", "shop/concept-home-cooking-with-female-chef.jpg", "products"),
    ("Childrens Bedroom", "shop/childrens-bed-nursery-cot-velvet-childrens-room.jpg", "Furnitureforkids"),
    ("Wooden dining chairs and table set", "shop/Victorian-Dining-Table.jpg", "products"),
    ("Wardrobe", "shop/Wooden-Wardrobe-Designs.jpg", "Wardrobe"),
    ("Elegant bedroom furniture", "shop/bedroomdesign.jpg", "products"),
]

COLLECTIONS = [
    ("Baby Cot", "BabyCot", "images/BabyCot/nwibc1a.jpeg"),
    ("Classic Ranges", "ClassicRanges", "images/classicranges/classicranges.jpg"),
    ("Skin Ranges", "SkinRanges", "images/skinrange/skinrangeone.jpeg"),
    ("Veneer Ranges", "VeneerRanges", "images/veneerrange/veneerrangeone.jpg"),
    ("Laminate Ranges", "LaminateRanges", "images/laminaterange/laminaterangeone.png"),
    ("Light Opening Ranges", "LightOpeningRanges", "images/lightopening/lightopeningdesigntwo.jpg"),
]

PRODUCT_FEATURES = [
    ("Explore Baby Cots", [
        "Neminath Wood presents a thoughtfully crafted range of baby cots designed to provide comfort, safety, and style for your little ones. Each cot is made with care to support peaceful sleep and a secure environment.",
        "With smooth finishes, strong construction, and elegant detailing, Neminath baby cots blend durability with gentle design, making them a perfect addition to any nursery.",
    ], "images/neminathproducts/products2.jpeg"),
    ("Custom Furniture & Interior Works", [
        "Neminath offers a refined range of custom furniture and interior solutions designed to enhance comfort, elegance, and functionality. Each piece is carefully crafted with attention to detail and smooth finishing.",
        "Our expertise includes soft leg designs, refined interior structures, and precise fitting that deliver both durability and visual appeal, ensuring every product blends seamlessly into your space.",
    ], "images/neminathproducts/product3.jpeg"),
    ("Study Sets", [
        "Neminath presents a thoughtfully designed range of study sets that combine comfort, functionality, and modern design. Each set is crafted to create a focused and organized learning environment for all age groups.",
        "With smooth finishes, smart storage solutions, and sturdy construction, our study sets are designed to support daily use while enhancing the overall look of your interior space.",
    ], "images/neminathproducts/product5.jpeg"),
    ("Custom Baby Cots", [
        "Neminath offers custom baby cots designed with care, comfort, and safety in mind. Each cot is thoughtfully created to meet individual requirements, ensuring a perfect fit for your nursery space.",
        "With smooth finishes, gentle edges, and sturdy construction, our custom baby cots provide a secure and comfortable environment while blending beautifully with your interior design.",
    ], "images/neminathproducts/product6.jpeg"),
]

_P = "images/neminathproducts/"
PRODUCT_GALLERY = [
    (_P + "product4.jpeg", "Skin Range Doors"),
    (_P + "product7.jpeg", "Elegant Skin Door"),
    (_P + "product8.jpeg", "Smooth Finish Door"),
    (_P + "product9.jpeg", "Premium Skin Door"),
    (_P + "product10.jpeg", "Durable Wood Door"),
    (_P + "product11.jpeg", "Stylish Interior Door"),
    (_P + "product12.jpeg", "Classic Wooden Door"),
    (_P + "product19.jpeg", "Modern Wooden Door"),
    (_P + "product13.jpeg", "Comfort Baby Cot"),
    (_P + "product14.jpeg", "Safe & Stylish Baby Cot"),
    (_P + "product15.jpeg", "Soft-Leg Design with Smooth Inner Wood Finish"),
    (_P + "product16.jpeg", "Elegant TV Setting with Clean Finish"),
    (_P + "product17.png", "Refined Inner Wood Finish with Thoughtful Detailing"),
    (_P + "product18.jpeg", "Carefully Finished Inner Wood for Lasting Comfort"),
]

BABYCOT_INTRO = {
    "image": "images/BabyCot/nwibc1a.jpeg",
    "eyebrow": "The NWI-BC series",
    "title": "Introduction to the NWI Baby Cot Collection",
    "paras": [
        "Our newest line under the NWI brand: precision-engineered baby cots built with child-safe, non-toxic finishes — designed in-house and manufactured to go beyond borders.",
        "A precision-engineered baby cot built on a dowel & barrel-nut joinery system for structural strength, offered across fixed and mobile variants — starting with our foundational model, NWI-BC-1A.",
    ],
}


# Door / finish ranges: intro block, about block, then a captioned gallery.
RANGES = {
    "classic": {
        "title": "Classic Ranges",
        "meta": "Classic range doors and furniture by Neminath Wood Industry, Chennai.",
        "intro_title": "Explore Classic Ranges",
        "intro": [
            "Neminath Wood offers a timeless selection of classic ranges that blend elegance and functionality for every interior space. Our designs are crafted to complement wooden finishes and modern décor effortlessly.",
            "From sophisticated cabinets to versatile furniture, Neminath's classic ranges provide quality, durability, and style, making every room both practical and aesthetically pleasing.",
        ],
        "intro_img": "images/classicranges/classicranges.jpg",
        "about_title": "Classic Ranges",
        "about": [
            "Neminath Wood presents a range of classic designs crafted to bring elegance and functionality to your interiors. Each piece is thoughtfully designed for lasting appeal.",
            "Our classic ranges combine quality craftsmanship and timeless style, ensuring every furniture piece enhances the beauty and comfort of your space.",
        ],
        "about_img": "images/classicranges/classicrangess.jpg",
        "gallery": [
            ("images/classicranges/classicrangeone.jpg", "Classic Range Doors"),
            ("images/classicranges/classicrangetwo.png", "Elegant Wooden Doors"),
            ("images/classicranges/classicrangethree.jpg", "Timeless Door Designs"),
            ("images/classicranges/classicrangefour.webp", "Premium Interior Doors"),
            ("images/classicranges/classicrangefive.jpg", "Sophisticated Door Styles"),
        ],
    },
    "skin": {
        "title": "Skin Ranges",
        "meta": "Skin doors by Neminath Wood Industry: smooth finishes, strength and versatility.",
        "intro_title": "Explore Skin Doors",
        "intro": [
            "Neminath Wood presents a premium selection of skin doors that combine sleek design with practical functionality for modern interiors. Each door is crafted to enhance the look of your spaces while maintaining durability.",
            "With smooth finishes and elegant detailing, Neminath's skin doors provide style, strength, and versatility, making every room both beautiful and functional.",
        ],
        "intro_img": "images/skinrange/skinrangeone.jpeg",
        "about_title": "Skin Doors",
        "about": [
            "Neminath Wood offers a collection of premium skin doors designed to add modern elegance and practical functionality to your interiors. Each door is crafted with precision for lasting appeal.",
            "Our skin doors combine sleek design and high-quality materials, ensuring every piece enhances the style and comfort of your space.",
        ],
        "about_img": "images/skinrange/skinrangetwo.webp",
        "gallery": [(f"images/skinrange/skinrange{n}.webp", "") for n in
                    ("three", "four", "five", "six", "seven", "eight", "nine", "ten")],
    },
    "veneer": {
        "title": "Veneer Ranges",
        "meta": "Veneer ranges by Neminath Wood Industry: natural textures and refined finishes.",
        "intro_title": "Explore Veneer Ranges",
        "intro": [
            "Neminath Wood presents premium veneer ranges designed to enhance interiors with natural textures and refined finishes. Each veneer surface is carefully selected to highlight the beauty of real wood.",
            "Blending durability with elegant design, Neminath’s veneer ranges offer versatile solutions that suit modern and classic interiors, adding warmth and sophistication to every space.",
        ],
        "intro_img": "images/veneerrange/veneerrangeone.jpg",
        "about_title": "Veneer Ranges",
        "about": [
            "Neminath Wood presents a refined range of veneer designs crafted to add natural elegance and warmth to your interiors. Each finish is carefully created for a premium look.",
            "Our veneer ranges blend quality craftsmanship with timeless wooden textures, ensuring every piece enhances the style and sophistication of your space.",
        ],
        "about_img": "images/veneerrange/veneerrangetwo.jpg",
        "gallery": [
            ("images/veneerrange/veneerrangesix.webp", "Wood Veneer Types"),
            ("images/veneerrange/veneerrangeeight.webp", "Smooth Veneer Finish"),
            ("images/veneerrange/veneerrangethree.jpg", "Veneer Range Doors"),
            ("images/veneerrange/veneerrangeseven.jpg", "Wood veneer Inlay patterns"),
            ("images/veneerrange/veneerrangefour.jfif", "Elegant Veneer"),
            ("images/veneerrange/veneerrangefive.avif", "Veneer Door Wardrobe"),
        ],
    },
    "laminate": {
        "title": "Laminate Ranges",
        "meta": "Laminate ranges by Neminath Wood Industry: durable, easy to maintain finishes.",
        "intro_title": "Explore Laminate Ranges",
        "intro": [
            "Neminath Wood offers a versatile selection of laminate ranges designed to bring style, durability, and easy maintenance to every interior space. Our finishes are created to suit both modern and classic interiors.",
            "From functional cabinets to elegant furniture surfaces, Neminath’s laminate ranges combine strength, quality, and visual appeal, making interiors both practical and visually refined.",
        ],
        "intro_img": "images/laminaterange/laminaterangeone.png",
        "about_title": "Laminate Ranges",
        "about": [
            "Neminath Wood presents a range of laminate designs crafted to offer durability and modern appeal for your interiors. Each surface is thoughtfully created for everyday use.",
            "Our laminate ranges combine quality materials and refined finishes, ensuring every furniture piece adds style, strength, and comfort to your space.",
        ],
        "about_img": "images/laminaterange/laminaterangetwo.jpg",
        "gallery": [
            ("images/laminaterange/laminaterangethree.webp", "Laminate Range Floor"),
            ("images/laminaterange/laminaterangefour.jpg", "Elegant Laminate Doors"),
            ("images/laminaterange/laminaterangefive.jpg", "Timeless Door Designs"),
            ("images/laminaterange/laminaterangesix.jpg", "Premium Interior Doors"),
            ("images/laminaterange/laminaterangeseven.webp", "Laminated Wood Furniture"),
            ("images/laminaterange/laminaterangeeight.jpg", "Refined Laminate Kitchens"),
        ],
    },
    "light": {
        "title": "Light Opening Ranges",
        "meta": "Light opening ranges by Neminath Wood Industry: brightness, openness and wooden finishes.",
        "intro_title": "Explore Light Opening Ranges",
        "intro": [
            "Neminath Wood offers a refined selection of light opening ranges designed to enhance brightness and openness in every interior space. Our designs are created to balance functionality with elegant wooden finishes.",
            "From thoughtfully designed panels to versatile interior solutions, Neminath’s light opening ranges deliver quality, durability, and visual clarity, making spaces feel open, practical, and inviting.",
        ],
        "intro_img": "images/lightopening/lightopeningdesigntwo.jpg",
        "about_title": "Light Opening Ranges",
        "about": [
            "Neminath Wood presents a range of light opening designs crafted to enhance openness and brightness in your interiors. Each element is thoughtfully designed for balanced functionality.",
            "Our light opening ranges combine quality craftsmanship and refined design, ensuring every solution improves both the look and comfort of your space.",
        ],
        "about_img": "images/lightopening/lightopeningdesignthree.jpg",
        "gallery": [
            ("images/lightopening/lightopeningdesignone.png", "Light Opening Ranges"),
            ("images/lightopening/lightopeningdesignfour.jpg", "Bright Space Ranges"),
            ("images/lightopening/lightopeningdesignfive.webp", "Open Light Designs"),
            ("images/lightopening/lightopeningdesignsix.webp", "Natural Light Solutions"),
            ("images/lightopening/lightopeningdesignseven.jpg", "Airy Interior Ranges"),
            ("images/lightopening/lightopeningdesigneight.webp", "Light Flow Designs"),
        ],
    },
}

# Residence and corporate pages: two text blocks and six captioned designs.
SPACES = {
    "wardrobe": {
        "title": "Wardrobe",
        "meta": "Premium wardrobe designs by Neminath Wood Industry that blend style and storage.",
        "a_title": "Wardrobe Solutions",
        "a": [
            "Neminath Wood offers premium wardrobe designs that blend style and functionality for your living spaces.",
            "Our expertly crafted wardrobes provide ample storage while enhancing the elegance of your home interiors.",
        ],
        "a_img": "images/wardrobe/wardrobe.webp",
        "b_title": "Wardrobe Designs",
        "b": [
            "Neminath Wood crafts elegant wardrobes that maximize storage while adding charm to any bedroom.",
            "Our designs combine functionality with style, ensuring each wardrobe meets both practical needs and aesthetic appeal.",
        ],
        "b_img": "images/wardrobe/wardrobeone.webp",
        "gallery": [
            ("images/wardrobe/wardrobethree.jpg", "Elegant Wardrobe"),
            ("images/wardrobe/wardrobefour.avif", "Smart Storage"),
            ("images/wardrobe/wardrobefive.avif", "Space Saver"),
            ("images/wardrobe/wardrobesix.webp", "Stylish Design"),
            ("images/wardrobe/wardrobeseven.jfif", "Functional Wardrobe"),
            ("images/wardrobe/wardrobeeight.avif", "Timeless Appeal"),
        ],
    },
    "tv": {
        "title": "TV Unit",
        "meta": "Stylish TV units by Neminath Wood Industry with premium finish and smart storage.",
        "a_title": "Introduction to a TV Unit",
        "a": [
            "Neminath Wood offers stylish and functional TV units crafted to enhance your living space. Each piece combines elegance with practical storage solutions.",
            "Our designs focus on premium quality, durability, and a perfect finish, making your entertainment area both organized and visually appealing.",
        ],
        "a_img": "images/Tvunit/tvunittwo.webp",
        "b_title": "TV Unit Designs",
        "b": [
            "Neminath Wood creates modern TV units that blend style and functionality, perfect for every living room setup.",
            "Our designs focus on premium craftsmanship, durable materials, and smart storage solutions to keep your space organized and elegant.",
        ],
        "b_img": "images/Tvunit/tvunitthree.jpg",
        "gallery": [
            ("images/Tvunit/tvunitfour.jpg", "Elegant Setup"),
            ("images/Tvunit/tvunitfive.avif", "Compact Design"),
            ("images/Tvunit/tvunitsix.jpg", "Modern Display"),
            ("images/Tvunit/tvunitseven.avif", "Stylish Storage"),
            ("images/Tvunit/tvuniteight.jpg", "Entertainment Hub"),
            ("images/Tvunit/tvunitnine.avif", "Living Room Focus"),
        ],
    },
    "kids": {
        "title": "Furniture for Kids",
        "meta": "Safe, stylish kids' furniture by Neminath Wood Industry.",
        "a_title": "Introduction to a Furniture for Kids",
        "a": [
            "Neminath Wood creates safe and stylish furniture designed specifically for children. Each piece combines comfort, durability, and modern design for a perfect kids’ space.",
            "Our products are crafted with care using high-quality materials, ensuring both functionality and elegance in every child’s room.",
        ],
        "a_img": "images/Furnitureforkids/kidsdesignone.jpg",
        "b_title": "Kids’ Furniture Designs",
        "b": [
            "Neminath Wood crafts furniture that brings comfort, safety, and creativity to children’s rooms. Every piece is designed to inspire fun and learning.",
            "Our expert craftsmanship ensures durable, stylish, and functional furniture that grows with your child, making their space both playful and practical.",
        ],
        "b_img": "images/Furnitureforkids/kidsdesigntwo.png",
        "gallery": [
            ("images/Furnitureforkids/kidsdesignthree.webp", "Sturdy Baby Cot"),
            ("images/Furnitureforkids/kidsdesignfour.avif", "Kid's Durable Wooden Desk"),
            ("images/Furnitureforkids/kidsdesignfive.avif", "Safe Kids Bed"),
            ("images/Furnitureforkids/kidsdesignsix.jpeg", "Organized Study Area"),
            ("images/Furnitureforkids/kidsdesignsevem.webp", "Natural Wood Finish"),
            ("images/Furnitureforkids/kidsdesigneight.jpg", "Kids’ Learning Space"),
        ],
    },
    "corporate": {
        "title": "Corporate",
        "meta": "Corporate interior solutions by Neminath Wood Industry for offices and commercial spaces.",
        "a_title": "Explore Corporate Solutions",
        "a": [
            "Neminath Wood offers a professional range of corporate interior solutions designed to support functional, organized, and modern workspaces. Our designs are created to suit offices, commercial spaces, and business environments.",
            "From smart storage units to refined furniture solutions, Neminath’s corporate range delivers quality, durability, and efficiency, helping create productive and visually balanced workspaces.",
        ],
        "a_img": "images/corporate/corporateone.webp",
        "b_title": "Corporate Solutions",
        "b": [
            "Neminath Wood presents a range of corporate designs crafted to bring elegance and functionality to professional interiors. Each piece is thoughtfully designed for lasting appeal.",
            "Our corporate solutions combine quality craftsmanship and modern style, ensuring every furniture piece enhances the efficiency and aesthetic of your workspace.",
        ],
        "b_img": "images/corporate/corporatetwo.webp",
        "gallery": [
            ("images/corporate/corporatethree.jpg", "Executive Desks"),
            ("images/corporate/corporatefour.webp", "Conference Tables"),
            ("images/corporate/corporatefive.webp", "Workstations"),
            ("images/corporate/corporatesix.avif", "Reception Units"),
            ("images/corporate/corporateseven.jpg", "Storage Cabinets"),
            ("images/corporate/corporateeight.webp", "Office Partitions"),
        ],
    },
}

SEASONING = {
    "hero_img": "images/seasoningchamber/seasoningchamber.png",
    "steps": [
        ("Advanced Seasoning Chambers", [
            "Neminath Wood utilizes state-of-the-art seasoning chambers to ensure every wooden product is perfectly treated for durability and stability. Our chambers maintain precise temperature and humidity for optimal results.",
            "From large planks to intricate wooden components, our seasoning process guarantees quality, longevity, and superior finish, making every product reliable and ready for premium interior applications.",
        ], "images/seasoningchamber/seasoningchamberone.png"),
        ("Precision Wood Treatment", [
            "At Neminath Wood, our seasoning chambers are designed to enhance the natural durability of timber. Each batch of wood undergoes a carefully monitored process to maintain its quality and structural integrity.",
            "This innovative treatment ensures that every piece is resilient, warp-free, and ideal for crafting premium furniture and interior solutions that last for years.",
        ], ""),
        ("Advanced Seasoning Chamber", [
            "Neminath Wood takes pride in offering state-of-the-art seasoning chambers designed to enhance the quality, durability, and longevity of all our wooden products. Our advanced seasoning process ensures that every piece of timber used in our furniture, cabinets, and interior solutions is carefully dried and stabilized, maintaining its natural beauty while reducing moisture-related defects such as warping, cracking, or splitting.",
            "Each seasoning chamber at Neminath Wood is equipped with modern technology that precisely controls temperature, humidity, and airflow, creating an optimal environment for wood treatment. This meticulous process not only preserves the natural grain and texture of the wood but also strengthens its structure, making it suitable for a wide range of interior applications including wardrobes, doors, modular kitchens, and furniture.",
        ], "images/seasoningchamber/seasoningchambertwo.webp"),
        ("Traditional craft, modern drying", [
            "By integrating traditional craftsmanship with modern drying techniques, Neminath Wood ensures that every product delivered to our clients is of superior quality, reliable, and long-lasting. Our commitment to using only perfectly seasoned wood reflects our dedication to excellence, allowing us to provide interior solutions that are both aesthetically pleasing and highly functional.",
            "Whether it’s classic ranges, laminate doors, veneer finishes, or corporate furniture, the foundation of all our products starts with properly seasoned wood, setting Neminath apart as a trusted name in premium interior solutions.",
        ], ""),
    ],
    "uses": ["Wardrobes", "Doors", "Modular kitchens", "Furniture", "Classic ranges", "Laminate doors", "Veneer finishes", "Corporate furniture"],
}
