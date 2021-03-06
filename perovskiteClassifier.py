import pandas as pd
import compoundObject as co




import time
start = time.time()

dataset = "Bandgap"   # Stability or Bandgap
# dataset = "Stability"

if (dataset ==  "Stability"): file = pd.read_csv('./data/Input.csv')     # Stability Dataset
if (dataset ==  "Bandgap"): file = pd.read_csv('./data/HSE_GGA.csv')     # Bandgap Dataset




try:
    atomList = list()
    moleculeComposition = list()
    organicCationsComposition = list()

    # organicAtoms = co.CompoundObject()
    nameOrganic = list()


    for i, composition in enumerate(file['Material composition']):
        # print(composition, ': ',eachCompound.getComposition(composition))
        # print(type(composition))
        eachCompound = co.CompoundObject(composition)
        moleculeComposition.append(eachCompound)

except KeyError:
    print("Make sure column called: Material composition exists.")

except LookupError:
    print("Something wrong with indexing. Check the searches.")

data = list()

for  x in moleculeComposition:
    # print("Composition: " ,x.materialComposition, "   Organic CationA:", x.cationA, "   CationB:", x.cationB, "   AnionX:", )
    data.append((x.materialComposition, x.cationA, x.cationB, x.anionX))


df = pd.DataFrame(data)
print(df.head())

df.to_csv("./output/perovskiteClassifierOutput.csv", sep=',')

