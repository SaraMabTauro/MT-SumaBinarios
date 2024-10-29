import tkinter as tk
from tkinter import messagebox

def binary_sum(bin1, bin2):
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    result = num1 + num2
    binary_result = bin(result)[2:]  
    return binary_result

def perform_sum():
    input_value = entry.get()
    
    if '+' not in input_value or input_value.count('+') > 1:
        messagebox.showerror("Error", "La entrada debe contener exactamente un signo '+'")
        return

    bin1, bin2 = input_value.split('+')
    
    if len(bin1) < 2 or len(bin2) < 1 or not all(c in '01' for c in bin1 + bin2):
        messagebox.showerror("Error", "Entrada inválida: los números deben ser binarios y tener al menos 2 y 1 bits respectivamente")
        return
    
    result = binary_sum(bin1, bin2) + "="
    
    result_label.config(text=f"Resultado: {result}")

root = tk.Tk()
root.title("Suma de Binarios con Máquina de Turing")
root.geometry("400x200")

tk.Label(root, text="Ingrese dos números binarios separados por '+':").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

sum_button = tk.Button(root, text="Sumar", command=perform_sum)
sum_button.pack(pady=10)

result_label = tk.Label(root, text="Resultado: ")
result_label.pack(pady=10)

root.mainloop()
