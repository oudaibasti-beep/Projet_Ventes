import pandas as pd
import matplotlib.pyplot as plt

# Load the file you just generated
df = pd.read_csv('ventes.csv', sep=';')

# 2. Calculate Chiffre d'Affaires Brut (Prix * Quantite)
df['CA_Brut'] = df['Prix'] * df['Quantite']

# 3. Calculate CA Net (Apply percentage discount)
df['CA_Net'] = df['CA_Brut'] * (1 - df['Remise'] / 100)

# 4. Calculate TVA (20% on CA Net)
df['TVA'] = df['CA_Net'] * 0.20

# 5. Calculate Total Company Revenue (CA Total)
total_ca = df['CA_Net'].sum()

# 6. Identify Product ID with the highest profit (CA Net)
top_product_id = df.loc[df['CA_Net'].idxmax(), 'ID']

# Display results in the terminal
print(f"--- RÉSULTATS ---")
print(f"Chiffre d'Affaires Total: {total_ca}")
print(f"Produit le plus rentable (ID): {top_product_id}")

# 7. Export to resultats_final.csv
df.to_csv('resultats_final.csv', index=False)
print(f"--- Fichier 'resultats_final.csv' exporté avec succès! ---")


df.plot(kind='bar', x='ID', y='CA_Net')
plt.title('CA par Produit')
plt.show()