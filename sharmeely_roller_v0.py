import random

def to_entries(collection):
    # Converts a dict into a list of (key, value) tuples;
    # otherwise returns the collection as-is.
    return list(collection.items()) if isinstance(collection, dict) else list(collection)

def roll_for_rarity(coatscommon, coatsuncommon, coatsrare, coatsextra, coatspedigree, coatsdesign, rarity):
    combined = []
    if rarity >= 1:
        combined += to_entries(coatscommon)
    if rarity >= 2:
        combined += to_entries(coatsuncommon)
    if rarity >= 3:
        combined += to_entries(coatsrare)
    if rarity >= 4:
        combined += to_entries(coatsextra)
    if rarity >= 5:
        combined += to_entries(coatspedigree)
    if rarity >= 6:
        combined += to_entries(coatsdesign)
    
    if not combined:
        raise ValueError("No coats available for the given rarity level.")
    
    selected = random.choice(combined)
    if isinstance(selected, tuple):
        phenotype, genotype = selected
    else:
        phenotype = genotype = selected
    return phenotype, genotype

def roll_for_multiple_markings(markings1, markings2, markings3, marking_choice, num_markings):
    if marking_choice == 1:
        pool = to_entries(markings1)
    elif marking_choice == 2:
        pool = to_entries(markings2)
    elif marking_choice == 3:
        pool = to_entries(markings3)
    else:
        raise ValueError("Invalid marking choice. Must be 1, 2, or 3.")
    
    if not pool or num_markings == 0:
        return None
    
    if num_markings <= len(pool):
        selected = random.sample(pool, num_markings)
    else:
        selected = [random.choice(pool) for _ in range(num_markings)]
    
    pheno_list = []
    geno_list = []
    for item in selected:
        if isinstance(item, tuple):
            pheno, geno = item
        else:
            pheno = geno = item
        pheno_list.append(pheno)
        geno_list.append(geno)
    
    return " ".join(pheno_list), " ".join(geno_list)

def roll_for_multiple_mutations(mutations1, mutations2, mutations3, mutation_choice, num_mutations):
    if mutation_choice == 1:
        pool = to_entries(mutations1)
    elif mutation_choice == 2:
        pool = to_entries(mutations2)
    elif mutation_choice == 3:
        pool = to_entries(mutations3)
    else:
        raise ValueError("Invalid mutation choice. Must be 1, 2, or 3.")
    
    if not pool or num_mutations == 0:
        return None
    
    if num_mutations <= len(pool):
        selected = random.sample(pool, num_mutations)
    else:
        selected = [random.choice(pool) for _ in range(num_mutations)]
    
    pheno_list = []
    geno_list = []
    for item in selected:
        if isinstance(item, tuple):
            pheno, geno = item
        else:
            pheno = geno = item
        pheno_list.append(pheno)
        geno_list.append(geno)
    
    return " ".join(pheno_list), " ".join(geno_list)

def roll_for_oddball(oddballs):
    # Ask the user if they want a random abnormality.
    answer = input("Get a random abnormality? (y/n): ").strip().lower()
    if answer.startswith("y"):
        # 10% chance to roll an oddball
        if random.random() < 0.1:
            pool = to_entries(oddballs)
            selected = random.choice(pool)
            if isinstance(selected, tuple):
                oddball_pheno, _ = selected  # only append to pheno
            else:
                oddball_pheno = selected
            return oddball_pheno
    return None

def combine_all_results(coat_result, markings_result, mutations_result, oddball_result):
    coat_pheno, coat_geno = coat_result
    mark_pheno, mark_geno = ("", "") if markings_result is None else markings_result
    mut_pheno, mut_geno = ("", "") if mutations_result is None else mutations_result
    
    # Combine coat, markings, and mutations (if any)
    combined_pheno = " ".join(filter(None, [coat_pheno, mark_pheno, mut_pheno]))
    combined_geno = " ".join(filter(None, [coat_geno, mark_geno, mut_geno]))
    
    # Append abnormality if rolled
    if oddball_result:
        combined_pheno += " + " + oddball_result
    
    return f"Phenotype: {combined_pheno}\nGenotype: {combined_geno}"

if __name__ == "__main__":
    # all basecoats
    coatscommon = {'Chestnut' : 'ee_', 'Bay' : 'E_ A_', 'Black' : 'E_ aa', 'Palomino' : 'ee_ Cr_', 'Buckskin' : 'E_ A_ Cr_', 'Smokey Black' : 'E_ aa Cr_'}
    coatsuncommon = {'Gold Champagne' : 'ee_ Ch_', 'Amber Champagne' : 'E_ A_ Ch_', 'Classic Champagne' : 'E_ aa Ch_', 'Gold Pearl' : 'ee_ prlprl', 'Amber Pearl' : 'E_ A_ prlprl', 'Black Pearl' : 'E_ aa prlprl', 'Bronze' : 'ee_ Pr_', 'Iron' : 'E_ A_ Pr_', 'Steel' : 'E_ aa Pr_', 'Clay' : 'ee_ stnstn', 'Shale' : 'E_ A_ stnstn', 'Granite' : 'E_ aa stnstn', 'Cherry' : 'ee_ Yn_', 'Cranberry' : 'E_ A_ Yn_', 'Rhubarb' : 'E_ aa Yn_', 'Powder Loden' : 'ee_ Th_', 'Pistachio Loden' : 'E_ A_ Th_', 'Classic Loden' : 'E_ aa Th_'}
    coatsrare = {'Gold Cream Champagne' : 'ee_ Cr_ Ch_', 'Amber Cream Champagne' : 'E_ A_ Cr_ Ch_', 'Classic Cream Champagne' : 'E_ aa Cr_ Ch_', 'Cremello' : 'ee_ CrCr', 'Perlino'  :  'E_ A_ CrCr', 'Smoky Cream'  :  'E_ aa CrCr', 'Brass'  :  'ee_ CrPr', 'Chrome'  :  'E_ A_ CrPr', 'Cobalt'  :  'E_ aa CrPr', 'Sand'  :  'ee_ Crstn', 'Silica'  :  'E_ A_ stn Cr_', 'Cobble'  :  'E_ aa stn Cr_', 'Sangria' : 'ee_ YnCr', 'Port' : 'E_ A_ YnCr', 'Velvet' : 'E_ aa YnCr', 'Coral' : 'ee_ Cr_ Th_', 'Seagrass' : 'E_ A_ Cr_ Th_', 'Yosun' : 'E_ aa Cr_ Th_', 'Palomino Pearl' : 'ee_ Crprl', 'Buckskin Pearl' : 'E_ A_ Crprl', 'Smoky Cream Pearl' : 'E_ aa Crprl', 'Honeybutter' : 'ee_ Pr_ Ch_', 'Tuscan' : 'E_ A_ Pr_ Ch_', 'Mustard' : 'E_ aa Pr_ Ch_', 'Gold Pearl Champagne' : 'ee_ prlprl Ch_', 'Bay Pearl Champagne' : 'ee_ prlprl Ch_', 'Black Pearl Champagne' : 'E_ aa prlprl Ch_', 'Chestnut Pearl Champagne' : 'E_ A_ prlprl Ch_', 'Palomino Pearl Champagne' : 'ee_ prlprl Ch_', 'Buckskin Pearl Champagne' : 'E_ A_ prlprl Ch_', 'Smoky Black Pearl Champagne' : 'E_ aa prlprl Ch_', 'Gold Pearl Champagne' : 'ee_ prlprl Ch_', 'Amber Pearl Champagne' : 'E_ A_ prlprl Ch_', 'Classic Pearl Champagne' : 'E_ aa prlprl Ch_', 'Gold Cream Pearl Champagne' : 'ee_ Crprl Ch_', 'Amber Cream Pearl Champagne' : 'E_ A_ Crprl Ch_', 'Classic Cream Pearl Champagne' : 'E_ aa Crprl Ch_'}
    coatsextra = {'Ash' : 'ee_ stnstn Ch_','Cinder' : 'E_ A_ stnstn Ch_','Charcoal' : 'E_ aa stnstn Ch_','Syrah' : 'ee_ Yn_ Ch_', 'Merlot' : 'E_ A_ Yn_ Ch_', 'Cabernet' : 'E_ aa Yn_ Ch_', 'Martini' : 'ee_ Th_ Ch_', 'Vermouth' : 'E_ A_ Th_ Ch_', 'Verdant' : 'E_ aa Th_ Ch_', 'Copper' : 'ee_ Prprl', 'Rose Gold' : 'E_ A_ Prprl', 'Tungsten' : 'E_ aa Prprl Ch_', 'Salt' : 'ee_ prlstn', 'Paprika' : 'E_ A_ prlstn Ch_', 'Pepper' : 'E_ aa prlstn Ch_', 'Moscato' : 'ee_ prlprl Yn_', 'Pink Moscato' : 'E_ A_ Yn_ prlprl Ch_', 'Chardonnay' : 'E_ aa Yn_ prlprl', 'Mint' : 'ee_ prlprl Th_', 'Basil' : 'E_ A_ prlprl Th_', 'Sage' : 'E_ aa Th_ prlprl', 'Vermillion' : 'ee_ Crprl Yn_', 'Scarlet' : 'E_ A_ Yn_ Crprl', 'Blood' : 'E_ aa Yn_ Crprl', 'Rosemary' : 'ee_ Crprl Th_', 'Thyme' : 'E_ A_ Th_ Crprl', 'Oregano' : 'E_ aa Th_ Crprl', 'Gold Cream Pearl Champagne' : 'ee_ Crprl Ch_', 'Amber Cream Pearl Champagne' : 'E_ A_ Crprl Ch_', 'Classic Cream Pearl Champagne' : 'E_ aa Crprl Ch_'}
    coatspedigree = {'Sparrow' : 'ee_ Prprl Ch_', 'Starling' : 'E_ A_ Pr_ prlprl Ch_', 'Raven' : 'E_ aa Prprl Ch_', 'Powder Blue' : 'ee_ prlstn Ch_', 'Russian Blue' : 'E_ A_ prlstn Ch_', 'Royal Blue' : 'E_ aa prlstn Ch_', 'Maroon' : 'ee_ prlprl Yn_ Ch_', 'Mulberry' : 'E_ A_ prlprl Yn_ Ch_', 'Mahogany' : 'E_ aa prlprl Yn_ Ch_', 'Conure' : 'ee_ prlprl Th_ Ch_', 'Peacock' : 'E_ A_ prlprl Th_ Ch_', 'Turaco' : 'E_ aa prlprl Th_ Ch_'}
    coatsdesign = {'Taro' : 'ee_ prlstn Ch_', 'Mauve' : 'E_ A_ prlstn Ch_', 'Murphy' : 'E_ A_ prlstn Ch_', 'Sapphire' : 'ee_ Prstn Ch_', 'Indigo' : 'E_ A_ Prstn Ch_', 'Obsidian' : 'E_ aa Prstn Ch_', 'Plum' : 'ee_ stnstn Yn_ Ch_', 'Prune' : 'E_ A_ stnstn Yn_ Ch_', 'Currant' : 'E_ aa stnstn Yn_ Ch_', 'Maple' : 'ee_ stnstn Th_ Ch_', 'Oak' : 'E_ A_ stnstn Th_ Ch_', 'Pine' : 'E_ aa stnstn Th_ Ch_', 'Ruby' : 'ee_ prlstn Yn_ Ch_', 'Jasper' : 'E_ A_ prlstn Yn_ Ch_', 'Garnet' : 'E_ aa prlstn Yn_ Ch_', 'Melon' : 'ee_ prlstn Th_ Ch_', 'Honeydew' : 'E_ A_ prlstn Th_ Ch_', 'Musk' : 'E_ aa prlstn Th_ Ch_', 'Peanut' : 'ee_ Crprl Yn_ Ch_', 'Almond' : 'E_ A_ Crprl Yn_ Ch_', 'Cashew' : 'E_ aa Crprl Yn_ Ch_', 'Sugarcane' : 'ee_ Crprl Th_ Ch_', 'Bamboo' : 'E_ A_ Crprl Th_ Ch_', 'Sorghum' : 'E_ aa Crprl Th_ Ch_', 'Mocha' : 'ee_ PrCr Yn_', 'Chocolate' : 'E_ A_ PrCr Yn_', 'Espresso' : 'E_ aa PrCr Yn_', 'Mead' : 'ee_ PrCr Th_', 'Sherry' : 'E_ A_ PrCr Th', 'Vermouth' : 'E_ aa PrCr Th'}

    #all markings
    markings1 = {'Flaxen' : 'ff_', 'Silver' : 'Z_', 'Sooty' : 'Sty_', 'Roan' : 'Rn_', 'Dun' : 'D_', 'Gray' : 'G_'}
    markings2 = {'Overo' : 'O_', 'Tobiano' : 'T_', 'Rabicano' : 'Rb_', 'Splash' : 'Spl_', 'Snowflake Appaloosa' : 'nLp', 'Blanket Appaloosa' : 'nLP patn', 'Leopard Appaloosa' : 'nLp patnpatn'}
    markings3 = {'Dominant White' : 'W_', 'Sabino' : 'Sb_', 'Varnish Roan Appaloosa' : 'LpLp', 'Snowcap Appaloosa' : 'LpLp patn', 'Fewspot Appaloosa' : 'LpLp patnpatn'}
    
    #mutations
    mutations1 = {'Rosal' : 'rlrl', 'Radish' : 'Rd_', 'Stained' : 'St_', 'Crest' : 'Cst_', 'Cornish' : 'crcr', 'Laced' : 'L_', 'Seraph' : 'Sph_'}
    mutations2 = {'Primal' : 'Pr_', 'Jaguar' : 'grgr', 'Sunsper' : 'Sp_', 'Willowed' : 'Wh_', 'Blotted' : 'Bb_', 'Exper' : 'xpxp'}
    mutations3 = {'Pheonix Syndrome' : 'PXS_', 'Caped' : 'Cpd_', 'Polaris' : 'plrplr', 'Crown' : 'Cw_', 'Hotspur' : 'Hp_', 'Reverse' : 'revrev', 'Docket' : 'dckdck'}
    
    #abnormalities
    oddballs = ['Heterochromia', 'Birdcatcher Spots', 'Bend-Or Spots', 'Vitiligo', 'Swarry', 'Undercoat', 'Chimera', 'Brindle', 'Shorthair', 'Emperor', 'Cift', 'Brindle']
    
    # Get user input for coat rarity.
    try:
        max_rarity = int(input("Enter the max rarity for coats (1-6): "))
        print("Rolling up to rarity", max_rarity, ".")
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit(1)
    
    # Roll for coat color
    coat_result = roll_for_rarity(coatscommon, coatsuncommon, coatsrare, coatsextra, coatspedigree, coatsdesign, max_rarity)
    
    # Ask for markings
    try:
        num_markings = int(input("How many markings? (0-3): "))
        if num_markings < 0 or num_markings > 3:
            raise ValueError
    except ValueError:
        print("Invalid input for markings. Please enter a number between 0 and 3.")
        exit(1)
    
    markings_result = None
    if num_markings > 0:
        try:
            marking_choice = int(input("Enter marking rarity (1 = markings1, 2 = markings2, 3 = markings3): "))
            if marking_choice not in (1, 2, 3):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3 for markings.")
            exit(1)
        
        markings_result = roll_for_multiple_markings(markings1, markings2, markings3, marking_choice, num_markings)
    
    # Ask for mutations
    try:
        num_mutations = int(input("How many mutations? (0-3): "))
        if num_mutations < 0 or num_mutations > 3:
            raise ValueError
    except ValueError:
        print("Invalid input for mutations. Please enter a number between 0 and 3.")
        exit(1)
    
    mutations_result = None
    if num_mutations > 0:
        try:
            mutation_choice = int(input("Enter mutation rarity (1 = mutations1, 2 = mutations2, 3 = mutations3): "))
            if mutation_choice not in (1, 2, 3):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3 for mutations.")
            exit(1)
        
        mutations_result = roll_for_multiple_mutations(mutations1, mutations2, mutations3, mutation_choice, num_mutations)
    
    # Roll for an oddball abnormality
    oddball_result = roll_for_oddball(oddballs)
    
    # Combine and display all results
    final_output = combine_all_results(coat_result, markings_result, mutations_result, oddball_result)
    print("\n" + final_output)