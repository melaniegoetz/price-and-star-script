import csv

with open('../goodImages1.csv', 'r+') as csvfile:
    with open('../goodImages11.csv', 'w') as csvOutput:
        reader = csv.reader(csvfile, delimiter='\t')
        csvWriter = csv.writer(csvOutput, delimiter='\t')
        all = []
        for row in reader:
            try:
                # print row[4]
                nutritionFacts = row[4]
            except:
                continue
            nutritionFactsRow = nutritionFacts.split()
            print nutritionFactsRow
            i = 0
            calories = 0
            sugar = 0
            sodium = 0
            transfat = 0
            satfat = 0
            fiber = 0
            vitaminsDV = []
            omega3 = 2
            o3fattyacids = 3
            for i in range(len(nutritionFactsRow)):
                if nutritionFactsRow[i] == 'Calories' and nutritionFactsRow[i + 1] != 'from' and nutritionFactsRow[
                            i - 1] != 'needs.':
                    calories = nutritionFactsRow[i + 1]
                elif nutritionFactsRow[i] == 'Sugars' and nutritionFactsRow[i + 1] != 'Protein' and nutritionFactsRow[
                            i + 1] != 'Sugar':
                    sugar = nutritionFactsRow[i + 1]
                elif nutritionFactsRow[i] == 'Sodium' and nutritionFactsRow[i + 1] != 'Less':
                    sodium = nutritionFactsRow[i + 1]
                elif nutritionFactsRow[i] == 'Trans':
                    transfat = nutritionFactsRow[i + 2]
                elif nutritionFactsRow[i] == 'Saturated' and nutritionFactsRow[i + 2] != 'Less':
                    satfat = nutritionFactsRow[i + 2]
                elif nutritionFactsRow[i] == 'Vitamin':
                    vitaminsDV.append(nutritionFactsRow[i + 2])
                elif nutritionFactsRow[i] == 'Fiber' and nutritionFactsRow[i + 1] != '25g' and nutritionFactsRow[
                            i + 1] != '<' and nutritionFactsRow[i + 1] != 'Sugars' and nutritionFactsRow[
                            i + 1] != 'Less':
                    fiber = nutritionFactsRow[i + 1]
                else:
                    continue
            # print fiber

            # formatting parsed numbers correctly
            if sugar != 0:
                sugar = float(sugar[:-1])
            if transfat != 0:
                transfat = float(transfat[:-1])
            if satfat != 0:
                satfat = float(satfat[:-1])
            if fiber != 0:
                fiber = float(fiber[:-1])
            vitaminsDVF = []
            for dv in vitaminsDV:
                # print dv
                if dv == '*':
                    continue
                vitaminsDVF.append(float(dv[:-1]))
                # print fiber

            calories = float(calories)
            if sodium != 0:
                sodium = float(sodium[:-2])
            # print fiber


            starpoints = 0

            # Trans/Sat Fats ALGO
            if (transfat + satfat) > 1 and (transfat + satfat) <= 2:
                starpoints = starpoints - 1
            if (transfat + satfat) > 2 and (transfat + satfat) <= 3:
                starpoints = starpoints - 2
            if (transfat + satfat) > 3:
                starpoints = starpoints - 3

            # Added Sugar ALGO
            addedsugarpercent = .1
            if (calories != 0):
                addedsugarpercent = sugar / calories * 100
            if addedsugarpercent <= .1 and addedsugarpercent != 0:
                starpoints = starpoints - 1
            if addedsugarpercent <= .25 and addedsugarpercent > .1:
                starpoints = starpoints - 2
            if addedsugarpercent <= .40 and addedsugarpercent > .25:
                starpoints = starpoints - 3
            if addedsugarpercent > .40:
                starpoints = starpoints - 11

            # Sodium ALGO
            if sodium <= 240 and sodium > 120:
                starpoints = starpoints - 1
            if sodium <= 360 and sodium > 240:
                starpoints = starpoints - 2
            if sodium > 360 and sodium <= 600:
                starpoints = starpoints - 3
            if sodium > 600:
                starpoints = sodium - 11

            # Fiber ALGO
            if fiber >= 3.75:
                starpoints = starpoints + 3
            if fiber >= 2.5 and fiber < 3.75:
                starpoints = starpoints + 2
            if fiber >= 1.25 and fiber < 2.5:
                starpoints = starpoints + 1

                # Whole grain
            if fiber > 1.5:  # whole grains additional boost
                starpoints = starpoints + 1

                # vitamins and minerals
            greaterThan10Count = 0
            greaterThan5Count = 0
            for dv in vitaminsDVF:
                if (dv > 10):
                    greaterThan10Count += 1
                elif (dv > 5):
                    greaterThan5Count += 1
            if (greaterThan10Count >= 2):
                starpoints = starpoints + 3
            elif (greaterThan10Count >= 1 or greaterThan5Count >= 2):
                starpoints = starpoints + 2
            elif (greaterThan5Count >= 1):
                starpoints = starpoints + 1

            guidingStars = 0

            # correction for inaccurate "added sugar", "added sodium", "o-3 fatty", "epa/dha"
            starpoints = starpoints + 5

            if starpoints < 0:
                guidingStars = 0
            if starpoints == 1 or starpoints == 2:
                guidingStars = 1
            if starpoints == 3 or starpoints == 4:
                guidingStars = 2
            if starpoints >= 5:
                guidingStars = 3

            print guidingStars
            row.append(guidingStars)
            csvWriter.writerow(row)




























