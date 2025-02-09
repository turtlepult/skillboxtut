#Задача 4. Великий и могучий

text_input = input("Введите текст: ").split()

print(f"Самое длинное слово, {max(len(word) for word in text_input)} букв")