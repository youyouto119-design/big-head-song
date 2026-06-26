import tkinter as tk
from tkinter import font
import requests
import threading
import time
from datetime import datetime
import json
import os

class CryptoTickerWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("🪙 实时加密行情 - 屏幕滚动")
        
        # 设置窗口样式 - Windows 11 风格
        self.root.geometry("1400x80")
        self.root.attributes('-topmost', True)  # 置顶
        self.root.attributes('-alpha', 0.95)   # 半透明
        
        # 配置配置文件路径
        self.config_file = "crypto_ticker_config.json"
        self.load_config()
        
        # 创建主框架
        main_frame = tk.Frame(root, bg='#0f172a', height=80)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.pack_propagate(False)
        
        # 创建滚动文本框
        self.text_label = tk.Label(
            main_frame,
            text="",
            bg='#0f172a',
            fg='#e2e8f0',
            font=('Segoe UI', 14, 'bold'),
            wraplength=1380,
            justify=tk.LEFT,
            padx=20,
            pady=15
        )
        self.text_label.pack(fill=tk.BOTH, expand=True)
        
        # 创建控制按钮框架
        control_frame = tk.Frame(main_frame, bg='#0f172a', height=30)
        control_frame.pack(fill=tk.X, padx=10)
        
        # 最小化按钮
        min_btn = tk.Button(
            control_frame,
            text="−",
            bg='#667eea',
            fg='white',
            bd=0,
            padx=8,
            pady=2,
            font=('Segoe UI', 12),
            command=self.minimize_window
        )
        min_btn.pack(side=tk.LEFT, padx=2)
        
        # 设置按钮
        settings_btn = tk.Button(
            control_frame,
            text="⚙",
            bg='#667eea',
            fg='white',
            bd=0,
            padx=8,
            pady=2,
            font=('Segoe UI', 12),
            command=self.open_settings
        )
        settings_btn.pack(side=tk.LEFT, padx=2)
        
        # 关闭按钮
        close_btn = tk.Button(
            control_frame,
            text="×",
            bg='#ef4444',
            fg='white',
            bd=0,
            padx=8,
            pady=2,
            font=('Segoe UI', 12),
            command=self.root.quit
        )
        close_btn.pack(side=tk.RIGHT, padx=2)
        
        # 数据存储
        self.cryptos = ['BTC', 'ETH', 'BNB', 'XRP', 'ADA']
        self.crypto_data = {}
        self.is_running = True
        
        # 启动更新线程
        self.update_thread = threading.Thread(target=self.update_loop, daemon=True)
        self.update_thread.start()
        
        # 初始化显示
        self.update_display()
    
    def load_config(self):
        """加载配置文件"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.cryptos = config.get('cryptos', ['BTC', 'ETH', 'BNB', 'XRP', 'ADA'])
            except:
                self.cryptos = ['BTC', 'ETH', 'BNB', 'XRP', 'ADA']
        else:
            self.cryptos = ['BTC', 'ETH', 'BNB', 'XRP', 'ADA']
    
    def save_config(self):
        """保存配置文件"""
        config = {'cryptos': self.cryptos}
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    
    def minimize_window(self):
        """最小化窗口到系统托盘"""
        self.root.withdraw()
        # 创建系统托盘菜单（简单实现）
        self.root.after(2000, self.restore_window)
    
    def restore_window(self):
        """恢复窗口"""
        self.root.deiconify()
    
    def open_settings(self):
        """打开设置窗口"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("设置")
        settings_window.geometry("400x300")
        settings_window.attributes('-topmost', True)
        settings_window.configure(bg='#1e293b')
        
        # 标题
        title = tk.Label(
            settings_window,
            text="币种设置",
            bg='#1e293b',
            fg='#e2e8f0',
            font=('Segoe UI', 14, 'bold'),
            pady=10
        )
        title.pack()
        
        # 币种列表
        list_frame = tk.Frame(settings_window, bg='#1e293b')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        tk.Label(
            list_frame,
            text="选择要显示的币种（用逗号分隔）:",
            bg='#1e293b',
            fg='#94a3b8',
            font=('Segoe UI', 10)
        ).pack(anchor=tk.W)
        
        crypto_entry = tk.Entry(
            list_frame,
            bg='#334155',
            fg='#e2e8f0',
            font=('Segoe UI', 11),
            insertbackground='#e2e8f0'
        )
        crypto_entry.insert(0, ','.join(self.cryptos))
        crypto_entry.pack(fill=tk.X, pady=5)
        
        # 刷新间隔
        tk.Label(
            list_frame,
            text="刷新间隔（秒）:",
            bg='#1e293b',
            fg='#94a3b8',
            font=('Segoe UI', 10)
        ).pack(anchor=tk.W, pady=(10, 0))
        
        interval_entry = tk.Entry(
            list_frame,
            bg='#334155',
            fg='#e2e8f0',
            font=('Segoe UI', 11),
            insertbackground='#e2e8f0'
        )
        interval_entry.insert(0, "30")
        interval_entry.pack(fill=tk.X, pady=5)
        
        # 保存按钮
        def save_settings():
            new_cryptos = [c.strip().upper() for c in crypto_entry.get().split(',')]
            self.cryptos = [c for c in new_cryptos if c]
            self.save_config()
            settings_window.destroy()
        
        save_btn = tk.Button(
            list_frame,
            text="保存设置",
            bg='#667eea',
            fg='white',
            font=('Segoe UI', 11, 'bold'),
            command=save_settings,
            padx=20,
            pady=8
        )
        save_btn.pack(pady=10)
    
    def get_crypto_id(self, symbol):
        """根据 Symbol 获取 CoinGecko ID"""
        symbol_map = {
            'BTC': 'bitcoin',
            'ETH': 'ethereum',
            'BNB': 'binancecoin',
            'XRP': 'ripple',
            'ADA': 'cardano',
            'SOL': 'solana',
            'DOT': 'polkadot',
            'LTC': 'litecoin',
            'DOGE': 'dogecoin',
            'TRX': 'tron',
            'AVAX': 'avalanche-2',
            'LINK': 'chainlink',
        }
        return symbol_map.get(symbol, symbol.lower())
    
    def fetch_crypto_data(self):
        """从 CoinGecko API 获取数据"""
        try:
            ids = [self.get_crypto_id(c) for c in self.cryptos]
            ids_str = ','.join(ids)
            
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids_str}&vs_currencies=usd,cny&include_24hr_change=true&include_market_cap=true"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            self.crypto_data = {}
            for symbol, crypto_id in zip(self.cryptos, ids):
                if crypto_id in data:
                    self.crypto_data[symbol] = data[crypto_id]
        except Exception as e:
            print(f"获取数据错误: {e}")
    
    def format_price(self, price):
        """格式化价格"""
        if price < 0.01:
            return f"${price:.8f}"
        elif price < 1:
            return f"${price:.6f}"
        elif price < 100:
            return f"${price:.4f}"
        else:
            return f"${price:.2f}"
    
    def format_market_cap(self, cap):
        """格式化市值"""
        if cap >= 1e9:
            return f"${cap/1e9:.1f}B"
        elif cap >= 1e6:
            return f"${cap/1e6:.1f}M"
        else:
            return f"${cap/1e3:.1f}K"
    
    def update_display(self):
        """更新显示内容"""
        if not self.crypto_data:
            self.text_label.config(text="加载中...")
            return
        
        # 构建显示文本
        display_parts = []
        for symbol in self.cryptos:
            if symbol in self.crypto_data:
                data = self.crypto_data[symbol]
                price = data.get('usd', 0)
                change = data.get('usd_24h_change', 0)
                market_cap = data.get('usd_market_cap', 0)
                
                # 根据涨跌改变颜色
                change_text = f"{change:+.2f}%" if change else "N/A"
                arrow = "▲" if change and change > 0 else "▼" if change and change < 0 else "→"
                
                # 格式化显示
                display_text = f"{symbol}: {self.format_price(price)} {arrow} {change_text}"
                
                # 添加市值信息
                if market_cap:
                    display_text += f" (市值: {self.format_market_cap(market_cap)})"
                
                display_parts.append(display_text)
        
        # 添加时间戳
        current_time = datetime.now().strftime("%H:%M:%S")
        display_text = "  |  ".join(display_parts)
        display_text = f"[{current_time}]  {display_text}"
        
        self.text_label.config(text=display_text)
    
    def update_loop(self):
        """后台更新循环"""
        while self.is_running:
            try:
                self.fetch_crypto_data()
                self.root.after(0, self.update_display)
                time.sleep(30)  # 每 30 秒更新一次
            except Exception as e:
                print(f"更新错误: {e}")
                time.sleep(10)


def main():
    root = tk.Tk()
    app = CryptoTickerWidget(root)
    root.mainloop()


if __name__ == "__main__":
    main()
