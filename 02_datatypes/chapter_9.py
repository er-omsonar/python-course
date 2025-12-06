essential_spices = {'cinamon','cardimom','ginger'}
optional_spices = {'cloves','black paper','ginger'}

all_spices = essential_spices | optional_spices
common_spices = essential_spices & optional_spices
only_in_essential = essential_spices - optional_spices

print(f"all spices {all_spices}")
print(f"common spices {common_spices}")
print(f"only in essentails {only_in_essential}")

print(f"{'cloves' in optional_spices}")