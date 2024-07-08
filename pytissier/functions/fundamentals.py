class main_fn():

    def shortcrust_pastry(self, butter_percentage, sugar_percentage, dough_type, sugar_type, liquid_type):
        """
        sources: https://www.fontelatavola.it/magiadeisaporiok/2016/02/09/la-pasta-frolla/
        """

        valid_dough_type = ['regular', 'whipped']
        if dough_type not in valid_dough_type:
            raise Exception("dough_type can eithe be: '"+ "', '".join(valid_dough_type) + "'")
        
        valid_sugar_types = ['icing', 'granulated']
        if sugar_type not in valid_sugar_types:
            raise Exception("sugar_type can eithe be: '"+ "', '".join(valid_sugar_types) + "'")
        
        valid_liquid_types = ['yolks', 'eggwhites', 'full_egg', 'water', 'milk', 'cream']
        if liquid_type not in valid_liquid_types:
            raise Exception("liquid_type can eithe be: '"+ "', '".join(valid_liquid_types) + "'")
        
        flower = 1000
        butter = flower*butter_percentage
        sugar = flower*sugar_percentage
        base = flower + butter + sugar
        liquids = -1

        match dough_type:
            case 'regular':

                match sugar_type:
                    case 'icing':

                        match liquid_type:
                            case 'yolks':          # base/10 + ((butter-500)/100)*-40
                                liquids = base/10 + ((butter-500)/100)*-40
                                
                            case 'eggwhites':
                                liquids = base/23 + ((butter-500)/100)*-35

                            case 'full_egg':
                                liquids = base/20 + ((butter-500)/100)*-35

                            case 'water':
                                liquids = base/21 + ((butter-500)/100)*-40

                            case 'milk':
                                liquids = base/16.5 + ((butter-500)/100)*-50

                            case 'cream':
                                liquids = base/14.5 + ((butter-500)/100)*-54

                    case 'granulated':
                        match liquid_type:
                            case 'yolks':
                                liquids = base/6 + ((butter-500)/100)*-75

                            case 'eggwhites':
                                liquids = base/14 + ((butter-500)/100)*-75

                            case 'full_egg':
                                liquids = base/12 + ((butter-500)/100)*-60

                            case 'water':
                                liquids = base/16 + ((butter-500)/100)*-62

                            case 'milk':
                                liquids = base/12.5 + ((butter-500)/100)*-80

                            case 'cream':
                                liquids = base/11 + ((butter-500)/100)*-65
                         
            case 'whipped':
            
                match sugar_type:
                    case 'icing':
                        
                        match liquid_type:
                            case 'yolks':
                                liquids = base/10 + ((butter-500)/100)*-40

                            case 'full_egg':
                                liquids = base/20 + ((butter-500)/100)*-35

                            case _:
                                raise Exception("whipped dough only supports liquid_type: 'yolks' or 'full_egg'")
                                
                    case 'granulated':
                        raise Exception("whipped dough does not support granulated sugar")
                
        return {
            'flower' : flower,
            'butter' : butter,
            sugar_type : sugar,
            liquid_type : int(liquids)
        }