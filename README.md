# 📈 实时金融价格滚动插件

一个简洁美观的电脑实时滚动金融价格小插件，支持实时显示股票价格、涨跌幅度等信息。

## ✨ 功能特性

- ✅ **实时价格显示** - 显示最新的股票价格
- ✅ **涨跌指示** - 清晰显示涨跌方向和幅度
- ✅ **动态管理** - 轻松添加/删除你关注的股票
- ✅ **响应式设计** - 完美适配各种屏幕
- ✅ **美观UI** - 现代化的界面设计
- ✅ **快速搜索** - 支持回车键快速添加
- ✅ **多标签页** - 概览、详情、图表三合一（高级版）
- ✅ **数据可视化** - 支持图表展示涨跌趋势

## 🚀 快速开始

### 方式一：直接打开
1. 下载 `stock-ticker.html` 或 `ticker-advanced.html` 文件
2. 用浏览器直接打开该文件
3. 开始使用！

### 方式二：本地服务器
```bash
# 使用 Python
python -m http.server 8000

# 使用 Node.js
npx http-server
```

然后访问 `http://localhost:8000/stock-ticker.html`

## 📖 使用说明

### 基础版（stock-ticker.html）
- 简洁清爽的界面
- 快速添加/删除股票
- 实时价格显示
- 完美适配手机和桌面

### 高级版（ticker-advanced.html）
- 三个标签页：概览、详情、图表
- 统计信息面板
- 详细的股票数据（P/E、市值、成交量等）
- 可视化图表
- 深色主题

## 📝 使用步骤

1. **添加股票**
   - 在输入框中输入股票代码（如：AAPL、GOOGL、MSFT）
   - 点击「添加」按钮或按 Enter 键

2. **查看信息**
   - 查看实时价格和涨跌幅
   - 高级版可查看详细数据和图表

3. **移除股票**
   - 点击对应股票卡片上的「移除」按钮

## 📊 支持的股票代码

### 美国股票
- **科技股**：AAPL (Apple)、GOOGL (Google)、MSFT (Microsoft)、TSLA (Tesla)、META (Meta)
- **其他热门股**：AMZN (Amazon)、NVDA (Nvidia)、AMD (AMD)、IBM (IBM)

### 加密货币（高级版）
- **BTC** - Bitcoin
- **ETH** - Ethereum

### 港股、A股
- 可通过转换对应代码添加

## 🔧 自定义配置

### 修改默认股票
在 JavaScript 代码中找到：
```javascript
let stocks = ['AAPL', 'GOOGL', 'MSFT']; // 修改这里
```

### 修改刷新间隔
```javascript
// 改为 5000 表示每 5 秒刷新一次
setInterval(() => {
    updateDisplay();
}, 30000); // 修改这个数字
```

### 修改颜色主题

在 CSS 中修改：
```css
/* 基础版 */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

button {
    background: #667eea;
}

/* 高级版 */
body {
    background: #0f172a;
}
```

## 🌐 集成真实API

当前使用模拟数据。要集成真实数据，可以使用以下 API：

### 1. Alpha Vantage (推荐免费)
```javascript
const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=YOUR_KEY`;
```

### 2. IEX Cloud
```javascript
const url = `https://cloud.iexapis.com/stable/quote/${symbol}?token=YOUR_TOKEN`;
```

### 3. Finnhub
```javascript
const url = `https://finnhub.io/api/v1/quote?symbol=${symbol}&token=YOUR_TOKEN`;
```

## 📦 项目结构

```
big-head-song/
├── stock-ticker.html       # 基础版
├── ticker-advanced.html    # 高级版
└── README.md              # 说明文档
```

## 🎨 截图说明

### 基础版特点
- 紫色渐变背景
- 白色卡片设计
- 简洁明了
- 移动端友好

### 高级版特点
- 深色主题
- 多标签页面
- 数据统计
- 图表展示
- 专业外观

## 💡 常见问题

**Q: 为什么显示的是模拟数据？**
A: 当前版本使用演示数据。集成真实 API 后会显示实时数据。

**Q: 可以添加多少个股票？**
A: 理论无限制，建议不超过 20 个以保持性能。

**Q: 支持其他语言吗？**
A: 当前为中文版本。可以通过修改 HTML 标签中的 `lang="zh-CN"` 和相应文字来支持其他语言。

**Q: 能否部署为浏览器扩展？**
A: 可以，需要打包成 Chrome Extension 或 Firefox Add-on。

**Q: 数据多久更新一次？**
A: 基础版 30 秒，高级版 10 秒。可在代码中修改。

## 🔒 安全提示

- 不要在代码中硬写 API 密钥
- 使用环境变量或后端代理保护敏感信息
- 定期检查 API 配额使用情况

## 📱 浏览器兼容性

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ 现代浏览器均支持

## 🚀 性能优化建议

1. 使用 CDN 加速静态资源
2. 启用浏览器缓存
3. 压缩 JavaScript 和 CSS
4. 使用后端 API 代理降低请求延迟
5. 实施请求频率限制

## 📄 许可证

MIT License - 可自由使用和修改

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 技术支持

如有问题，欢迎通过以下方式联系：
- 提交 GitHub Issue
- 提交 Pull Request 建议

---

**享受实时金融数据吧！** 📈💰

**最后更新**: 2026-06-26