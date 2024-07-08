class main_fn():

    def shortcrust_pastry(self, butter_percentage, sugar_percentage, sugar_type, liquid_type):
        """
        sources: https://www.fontelatavola.it/magiadeisaporiok/2016/02/09/la-pasta-frolla/
        """

        valid_sugar_types = ['icing_sugar', 'granulated_sugar']
        if sugar_type not in valid_sugar_types:
            raise Exception("sugar_type can eithe be: '"+ "', '".join(valid_sugar_types) + "'")
        
        valid_liquid_types = ['yolks', 'eggwhites', 'full_egg', 'water', 'milk', 'cream']
        if liquid_type not in valid_liquid_types:
            raise Exception("sugar_type can eithe be: '"+ "', '".join(valid_liquid_types) + "'")
        
        flower = 1000
        butter = flower*butter_percentage
        sugar = flower*sugar_percentage
        base = flower + butter + sugar

        match sugar_type:
            case 'icing_sugar':
        
                match liquid_type:
                    case 'yolks':
                        match butter:
                            case 400:
                                liquids = base/10 + 40
                            case 500:
                                liquids = base/10
                            case 600:
                                liquids = base/10 - 40

                    case 'eggwhites':
                        match butter:
                            case 400:
                                liquids = base/23 + 35
                            case 500:
                                liquids = base/23
                            case 600:
                                liquids = base/23 - 35

                    case 'full_egg':
                        match butter:
                            case 400:
                                liquids = base/20 + 35
                            case 500:
                                liquids = base/20
                            case 600:
                                liquids = base/20 - 35

                    case 'water':
                        match butter:
                            case 400:
                                liquids = base/21 + 40
                            case 500:
                                liquids = base/21
                            case 600:
                                liquids = base/21 - 40

                    case 'milk':
                        match butter:
                            case 400:
                                liquids = base/16.5 + 50
                            case 500:
                                liquids = base/16.5
                            case 600:
                                liquids = base/16.5 - 50

                    case 'cream':
                        match butter:
                            case 400:
                                liquids = base/14.5 + 54
                            case 500:
                                liquids = base/14.5
                            case 600:
                                liquids = base/14.5 - 54

            case 'granulated_sugar':
        
                match liquid_type:
                    case 'yolks':
                        match butter:
                            case 400:
                                liquids = base/6 + 75
                            case 500:
                                liquids = base/6
                            case 600:
                                liquids = base/6 - 75

                    case 'eggwhites':
                        match butter:
                            case 400:
                                liquids = base/14 + 75
                            case 500:
                                liquids = base/14
                            case 600:
                                liquids = base/14 - 75

                    case 'full_egg':
                        match butter:
                            case 400:
                                liquids = base/12 + 60
                            case 500:
                                liquids = base/12
                            case 600:
                                liquids = base/12 - 60

                    case 'water':
                        match butter:
                            case 400:
                                liquids = base/16 + 62
                            case 500:
                                liquids = base/16
                            case 600:
                                liquids = base/16 - 62

                    case 'milk':
                        match butter:
                            case 400:
                                liquids = base/12.5 + 80
                            case 500:
                                liquids = base/12.5
                            case 600:
                                liquids = base/12.5 - 80

                    case 'cream':
                        match butter:
                            case 400:
                                liquids = base/11 + 65
                            case 500:
                                liquids = base/11
                            case 600:
                                liquids = base/11 - 65

        return {
            'flower' : flower,
            'butter' : butter,
            sugar_type : sugar,
            liquid_type : int(liquids)
        }