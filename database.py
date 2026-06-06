"""
Database module untuk CHECKCOMCHEMISTRY
Menyimpan data bahan kimia dan fungsi-fungsi terkait
"""

def get_chemical_database():
    """
    Mengembalikan database bahan kimia dengan kategori FCOT
    Returns: dict dengan format {nama_bahan: kategori}
    """
    chemicals = {
        # FLAMMABLE CHEMICALS (F)
        "Etanol": "Flammable",
        "Metanol": "Flammable",
        "Acetone": "Flammable",
        "Benzene": "Flammable",
        "Toluene": "Flammable",
        "Xylene": "Flammable",
        "Petroleum Ether": "Flammable",
        "Hexane": "Flammable",
        "Pentane": "Flammable",
        "Diethyl Ether": "Flammable",
        "Glycerin": "Flammable",
        "Turpentine": "Flammable",
        "Kerosene": "Flammable",
        "Diesel": "Flammable",
        "Gasoline": "Flammable",
        "Propane": "Flammable",
        "Butane": "Flammable",
        "Acetylene": "Flammable",
        "Hydrogen": "Flammable",
        "Methane": "Flammable",
        
        # CORROSIVE CHEMICALS (C)
        "Hydrochloric Acid (HCl)": "Corrosive",
        "Sulfuric Acid (H2SO4)": "Corrosive",
        "Nitric Acid (HNO3)": "Corrosive",
        "Phosphoric Acid (H3PO4)": "Corrosive",
        "Acetic Acid": "Corrosive",
        "Sodium Hydroxide (NaOH)": "Corrosive",
        "Potassium Hydroxide (KOH)": "Corrosive",
        "Calcium Hydroxide": "Corrosive",
        "Ammonia Solution": "Corrosive",
        "Hydrofluoric Acid (HF)": "Corrosive",
        "Sodium Hypochlorite": "Corrosive",
        "Hydrogen Peroxide (H2O2)": "Corrosive",
        "Formic Acid": "Corrosive",
        "Chlorine Water": "Corrosive",
        "Bromine": "Corrosive",
        "Chlorine Gas": "Corrosive",
        "Fluorine": "Corrosive",
        "Iodine": "Corrosive",
        "Sodium Carbonate": "Corrosive",
        "Potassium Carbonate": "Corrosive",
        
        # OXIDIZER CHEMICALS (O)
        "Potassium Permanganate (KMnO4)": "Oxidizer",
        "Potassium Dichromate": "Oxidizer",
        "Sodium Nitrate (NaNO3)": "Oxidizer",
        "Potassium Nitrate (KNO3)": "Oxidizer",
        "Calcium Nitrate": "Oxidizer",
        "Hydrogen Peroxide (H2O2) High": "Oxidizer",
        "Sodium Chlorite": "Oxidizer",
        "Potassium Permanganate": "Oxidizer",
        "Barium Nitrate": "Oxidizer",
        "Sodium Periodate": "Oxidizer",
        "Ammonium Nitrate": "Oxidizer",
        "Potassium Chlorate": "Oxidizer",
        "Sodium Chlorate": "Oxidizer",
        "Lead Nitrate": "Oxidizer",
        "Chromic Acid": "Oxidizer",
        "Iodine Pentoxide": "Oxidizer",
        "Peracetic Acid": "Oxidizer",
        "Bromate": "Oxidizer",
        "Ozone": "Oxidizer",
        "Chlorine Dioxide": "Oxidizer",
        
        # TOXIC CHEMICALS (T)
        "Mercury": "Toxic",
        "Lead": "Lead",
        "Arsenic": "Toxic",
        "Cadmium": "Toxic",
        "Cyanide": "Toxic",
        "Sodium Cyanide": "Toxic",
        "Potassium Cyanide": "Toxic",
        "Strychnine": "Toxic",
        "Pesticide": "Toxic",
        "Chloroform": "Toxic",
        "Carbon Tetrachloride": "Toxic",
        "Trichloroethylene": "Toxic",
        "Tetrachloroethylene": "Toxic",
        "Benzidine": "Toxic",
        "Dioxin": "Toxic",
        "Formaldehyde": "Toxic",
        "Chromium": "Toxic",
        "Nickel": "Toxic",
        "Beryllium": "Toxic",
        "Thallium": "Toxic",
        
        # ADDITIONAL CHEMICALS
        "Calcium Chloride": "Oxidizer",
        "Sodium Chloride": "Oxidizer",
        "Magnesium Chloride": "Oxidizer",
        "Copper Sulfate": "Oxidizer",
        "Iron Sulfate": "Oxidizer",
        "Aluminum Sulfate": "Oxidizer",
        "Zinc Sulfate": "Oxidizer",
        "Manganese Sulfate": "Oxidizer",
        "Nickel Sulfate": "Oxidizer",
        "Cobalt Sulfate": "Oxidizer",
        "Sodium Sulfate": "Oxidizer",
        "Potassium Sulfate": "Oxidizer",
        "Magnesium Sulfate": "Oxidizer",
        "Calcium Sulfate": "Oxidizer",
        "Barium Sulfate": "Oxidizer",
        "Lead Sulfate": "Oxidizer",
        "Copper Chloride": "Oxidizer",
        "Iron Chloride": "Oxidizer",
        "Aluminum Chloride": "Oxidizer",
        "Zinc Chloride": "Oxidizer",
        "Sodium Nitrite": "Oxidizer",
        "Potassium Iodide": "Oxidizer",
        "Sodium Iodide": "Oxidizer",
        "Potassium Bromide": "Oxidizer",
        "Sodium Bromide": "Oxidizer",
        "Sodium Fluoride": "Corrosive",
        "Sodium Sulfite": "Oxidizer",
        "Sodium Bisulfite": "Oxidizer",
        "Potassium Permanganate Solution": "Oxidizer",
        "Alcohol": "Flammable",
        "Isopropanol": "Flammable",
        "Propanol": "Flammable",
        "Butanol": "Flammable",
        "Pentanol": "Flammable",
        "Phenol": "Corrosive",
        "Creosol": "Corrosive",
        "Aniline": "Toxic",
        "Benzidine Base": "Toxic",
        "Naphthylamine": "Toxic",
        "Phenanthrene": "Toxic",
        "Anthracene": "Flammable",
        "Naphthalene": "Flammable",
        "Styrene": "Flammable",
        "Vinyl Chloride": "Flammable",
        "Acrylic Acid": "Corrosive",
        "Methacrylic Acid": "Corrosive",
        "Maleic Anhydride": "Corrosive",
        "Phthalic Anhydride": "Corrosive",
        "Terephthalic Acid": "Corrosive",
        "Isophthalic Acid": "Corrosive",
        "Tartaric Acid": "Corrosive",
        "Citric Acid": "Corrosive",
        "Lactic Acid": "Corrosive",
        "Glutaric Acid": "Corrosive",
        "Adipic Acid": "Corrosive",
        "Pimelic Acid": "Corrosive",
        "Suberic Acid": "Corrosive",
    }
    return chemicals

def get_ghs_images():
    """
    Mengembalikan mapping kategori ke emoji GHS
    Returns: dict dengan format {kategori: emoji}
    """
    return {
        "Flammable": "🔥",
        "Corrosive": "🧪",
        "Oxidizer": "⚡",
        "Toxic": "☠️",
        "Lead": "☠️"
    }

def get_chemical_info(chemical_name):
    """
    Mengambil informasi detail tentang bahan kimia tertentu
    
    Args:
        chemical_name (str): Nama bahan kimia
    
    Returns:
        dict: Informasi bahan kimia (nama, kategori, deskripsi)
    """
    db = get_chemical_database()
    if chemical_name in db:
        return {
            "name": chemical_name,
            "category": db[chemical_name],
            "icon": get_ghs_images().get(db[chemical_name], "🧪")
        }
    return None

def search_chemicals(keyword):
    """
    Mencari bahan kimia berdasarkan keyword
    
    Args:
        keyword (str): Kata kunci pencarian
    
    Returns:
        list: Daftar bahan kimia yang cocok
    """
    db = get_chemical_database()
    results = []
    keyword_lower = keyword.lower()
    
    for name, category in db.items():
        if keyword_lower in name.lower() or keyword_lower in category.lower():
            results.append({"name": name, "category": category})
    
    return results

def get_chemicals_by_category(category):
    """
    Mengambil semua bahan kimia berdasarkan kategori
    
    Args:
        category (str): Kategori FCOT (Flammable, Corrosive, Oxidizer, Toxic)
    
    Returns:
        list: Daftar bahan kimia dalam kategori tersebut
    """
    db = get_chemical_database()
    results = []
    
    for name, cat in db.items():
        if cat.lower() == category.lower():
            results.append(name)
    
    return results

def get_category_count():
    """
    Menghitung jumlah bahan kimia per kategori
    
    Returns:
        dict: Jumlah bahan kimia per kategori
    """
    db = get_chemical_database()
    count = {}
    
    for name, category in db.items():
        if category not in count:
            count[category] = 0
        count[category] += 1
    
    return count
