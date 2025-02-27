#Liam Duffy 
#CSCI 128 
#Time 3 hours


num_rounds = int(input("NUM ROUNDS> "))
num_stocks = int(input("NUM STOCKS> "))

Stocks = {}
Initial_Investments = {}

for _ in range(num_stocks):
    Stock_Ticker = input("TICKER> ")
    Initial_Investment = float(input("INITIAL INVESTMENT> "))
    Stocks[Stock_Ticker] = Initial_Investment
    Initial_Investments[Stock_Ticker] = Initial_Investment

for _ in range(num_rounds):
    Performance = input(f"SIM PERIOD {_ + 1}> ")
    Performance_Data = Performance.split(";")

    for i in range(0, len(Performance_Data), 2):
        Ticker = Performance_Data[i]
        Change = float(Performance_Data[i + 1])

        if Ticker in Stocks:
            Value = Stocks[Ticker]
            Change_Amount = Value * Change

            if Value + Change_Amount < 0:
                Stocks[Ticker] = 0
            else:
                Stocks[Ticker] += Change_Amount

    Total_Initial_Investment = sum(Initial_Investments.values())
    Total_Final_Value = sum(Stocks.values())

    for ticker, final_value in Stocks.items():
        initial_value = Initial_Investments[ticker]
        Change_Percentage = ((final_value - initial_value) / initial_value) * 100

        if Change_Percentage < 0:
            print(f"{ticker}: Loss {Change_Percentage:.2f}%")
        else:
            print(f"{ticker}: Gain {Change_Percentage:.2f}%")

    Overall_Change = ((Total_Final_Value - Total_Initial_Investment) / Total_Initial_Investment) * 100
    print(f"Overall: {Total_Initial_Investment:.2f} -> {Total_Final_Value:.2f} {Overall_Change:.2f}%")

