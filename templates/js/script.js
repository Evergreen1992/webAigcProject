// 模拟数据 (通常会从服务器获取)
const data = [
    {
        img: 'https://via.placeholder.com/400x300',
        title: '示例标题 1',
        authorImg: 'https://via.placeholder.com/40',
        authorName: '作者名 1'
    },
    {
        img: 'https://via.placeholder.com/400x300',
        title: '示例标题 2',
        authorImg: 'https://via.placeholder.com/40',
        authorName: '作者名 2'
    },
    // 可以继续添加更多数据项...
];

// 初始化瀑布流
function initWaterfall() {
    const waterfall = document.getElementById('waterfall');

    data.forEach(item => {
        // 创建瀑布流项
        const waterfallItem = document.createElement('div');
        waterfallItem.className = 'waterfall-item';

        const img = document.createElement('img');
        img.src = item.img;

        const info = document.createElement('div');
        info.className = 'info';

        const title = document.createElement('h2');
        title.textContent = item.title;

        const author = document.createElement('div');
        author.className = 'author';

        const authorImg = document.createElement('img');
        authorImg.src = item.authorImg;

        const authorName = document.createElement('p');
        authorName.textContent = item.authorName;

        // 组装元素
        author.appendChild(authorImg);
        author.appendChild(authorName);
        info.appendChild(title);
        info.appendChild(author);
        waterfallItem.appendChild(img);
        waterfallItem.appendChild(info);
        waterfall.appendChild(waterfallItem);
    });
}

// 页面加载完成后初始化瀑布流
window.onload = initWaterfall;

// 无限下滑加载更多项
window.onscroll = function() {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        // 加载更多数据项...
        // 注意：实际产品中应该通过API从服务器获取新数据
        initWaterfall();
    }
};
