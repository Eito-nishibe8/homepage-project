document.addEventListener("DOMContentLoaded", function () {
    const headerHeight = document.querySelector("header").offsetHeight; // 固定ヘッダーの高さ
    const links = document.querySelectorAll("a[href^='#']");

    links.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault(); // デフォルトのジャンプを防ぐ
            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: "smooth"
                });
            }
        });
    });
});
