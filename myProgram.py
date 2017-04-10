def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

rate = input("Enter the rate of the conversion: ")
print("Rate is " + rate)
euros = input("Enter the money ammount you want to convert in $: ")
print("Euros is " + euros)

print(currency_converter(int(rate),int(euros)))
