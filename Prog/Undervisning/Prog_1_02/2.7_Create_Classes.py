from person import Person     
    
# Rui=Person() # Create Person-object without constructor-method
# Rui.name="Rui"
# Rui.age=27
# Rui.country="Spain"
# Rui.description()
# 
# 
# Louise=Person() # Create Person-object without constructor-method
# Louise.name="Louis"
# Louise.age=42
# Louise.country="USA"
# Louise.description()
# 
# Theodore=Person() # Create Person-object without constructor-method
# Theodore.name="Theodore"
# Theodore.age=18
# Theodore.country="The Land Down Under"
# Theodore.description()

Samuel=Person("Samuel",20,"Denmark") # Create Person-object with Constructor-method
Samuel.description()

Samuel=Person("Denmark",20,"Samuel") # Create Person-object with Constructor-method
Samuel.description()
