#Nombre: Brayan Stiven Rojas
# Grupo:
# Cod Estudiante: 202310325

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

#!!IMPORTANTE!! La funcion termina cuando se ingresa el cero y no lo tiene en cuenta

# INICIO SOLUCIÓN
n = 1                                                 #1
par = impar = 0                                       #1
while n != 0:                                         #n+1
    n=int(input("Ingrese un numero: "))               #n
    if n > 0:                                         #n
        if n % 2==0:                                  #n ( que la condicion sea verdadera)
            par += 1                                  #n ( que la condicion sea verdadera)
        else:                                         #n ( que la condicion sea verdadera)
            impar += 1                                #n ( que la condicion sea verdadera)
print("El total de numeros pares es: ",par)           #1
print("El total de numeros impares es: ",impar)       #1
# FIN SOLUCIÓN

#El orden de magnitun es O(n) donde n es el numero de veces que el usuario ingresa un numero
######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# INICIO SOLUCIÓN
print("Ingrese un numero: ")                #1
num = int(input())                          #1
fact = 1                                    #1
for i in range(1, num+1):                   #n
    fact*=i                                 #n
print("El factorial de ",num,"es: ",fact)   #1
# FIN SOLUCIÓN

#El orden de magnitud es O(n) ya que la cantidad de iteraciones del algoritmo depende del numero ingresado

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cmath>

using namespace std;

const int TM = 100;

bool esMatrizIdentidad(int matriz[TM][TM], int tamaño) {
    for (int i = 0; i < tamaño; ++i) {
        for (int j = 0; j < tamaño; ++j) {
            if (i == j) {
                if (matriz[i][j] != 1) {
                    return false;
                }
            } else {
                // Elementos fuera de la diagonal principal deben ser 0
                if (matriz[i][j] != 0) {
                    return false;
                }
            }
        }
    }
    return true;
}
int ordenMagnitud(int T) {
    return to_string(abs(T)).length();
}

int main() {
    unordered_map<int, int> frecuencias;
    vector<int> T;
    int T;
    int matriz[TM][TM];

    cout << "Ingrese el tamaño de la matriz cuadrada: ";
    cin >> T;

    cout << "Ingrese los elementos de la matriz:";
    for (int i = 0; i < T; ++i) {
        for (int j = 0; j < T; ++j) {
            cin >> matriz[i][j];
        }
    }

    if (esMatrizIdentidad(matriz, T)) {
        cout << "La matriz es una matriz identidad.";
    } else {
        cout << "La matriz no es una matriz identidad.";
    }
    while (cin >> T) {
        numeros.push_back(T);
        frecuencias[T]++;
    }

    cout << "Frecuencias de los números:";
    for (const auto& par : frecuencias) {
        int num = par.first;
        int freq = par.second;
        cout << "El número " << num << " aparece " << freq << " vez/veces.";
    }

    cout << "Orden de magnitud de los números:";
    for (const auto& num : numeros) {
        cout << "El número " << num << " tiene un orden de magnitud de " << ordenMagnitud(num) << " (cantidad de dígitos).";
    }
######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# INICIO SOLUCIÓN
n1 = int(input("Ingrese el numero a dividir: "))  #1
n2 = int(input("Ingrese el divisor: "))           #1
resultado = 0                                     #1
while n1 >= n2:                                   #n+1
    n1 -= n2                                      #n
    resultado += 1                                #n
print("El resultado es:", resultado)              #1
print("El residuo es:", n1)                       #1
# FIN SOLUCIÓN

#El orden de magnitud es O(n1/n2)
######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# INICIO SOLUCIÓN
cadena = input("Cadena de texto: ")              #1
cadena = cadena.replace(" ", "").lower()         #1
esPalindromo = True                              #1
for i in range(len(cadena) // 2):                #n/2
    if cadena[i] != cadena[-(i + 1)]:            #n/2
        esPalindromo = False                     #1
        break                                    #1
if esPalindromo:                                 #1
    print("La cadena es palindroma")             #1
else:                                            #1
    print("La cadena no es palindroma")          #1
# FIN SOLUCIÓN

#El orden de magnitud es O(n)
######################################
#                                    #
#             Punto #6               #
#                                    #
######################################

# INICIO SOLUCIÓN
n = int(input("Tamaño del arreglo: "))              #1
arreglo = []                                        #1
for i in range(n):                                  #n
    num = int(input(f"Ingrese el numero {i+1}: "))  #n
    arreglo.append(num)                             #n
max = arreglo[0]                                    #1
min = arreglo[0]                                    #1
for num in arreglo:                                 #n
    if num > max:                                   #n
        max = num                                   #n
    if num < min:                                   #n
        min = num                                   #n
print("El valor maximo es:",max)                    #1
print("El valor minimo es:",min)                    #1
# FIN SOLUCIÓN

#El orden de magnitud 0(n), n es el tamaño del arreglo
######################################
#                                    #
#             Punto #7               #
#                                    #
######################################

# INICIO SOLUCIÓN
num = int(input("Ingrese el numero: "))                     #1
exponente = int(input("Ingrese el exponente: "))            #1
resultado = 1                                               #1
for _ in range(exponente):                                  #n
    resultado *= num                                        #n
print(f"{num} elevado a la {exponente} es: {resultado}")    #1
# FIN SOLUCIÓN

#El orden de magnitud es O(n)
