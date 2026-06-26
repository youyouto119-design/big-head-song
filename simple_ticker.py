import tkinter as tk
import requests
import threading
import time

class SimpleCryptoTicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("💰 行情")
        self.root.geometry("1400x60")
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)
        self.root.configure(bg='#0f172a')
        
        self.label = tk.Label(self.root, text="加载中...", bg='#0f172a', fg='#f7931a', 
                             font=('Arial', 12, 'bold'), padx=20)
        self.label.pack(fill=tk.BOTH, expand=True)
        
        self.cryptos = ['BTC', 'ETH', 'BNB', 'XRP', 'ADA']
        threading.Thread(target=self.update_loop, daemon=True).start()
        
    def update_loop(self):
        while True:
            try:
                ids = 'bitcoin,ethereum,binancecoin,ripple,cardano'
                url = f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true'
                data = requests.get(url, timeout=5).json()
                
                text = ""
                for i, crypto_id in enumerate(['bitcoin', 'ethereum', 'binancecoin', 'ripple', 'cardano']):
                    if crypto_id in data:
                        price = data[crypto_id]['usd']
                        change = data[crypto_id]['usd_24h_change']
                        arrow = "▲" if change > 0 else "▼"
                        color = '#10b981' if change > 0 else '#ef4444'
                        text += f"{self.cryptos[i]}: ${price:.2f} {arrow}{change:.2f}%  |  "
                
                self.root.after(0, lambda: self.label.config(text=text[:-5]))
                time.sleep(30)
            except:
                time.sleep(10)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SimpleCryptoTicker()
    app.run()
