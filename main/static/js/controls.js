document.addEventListener("DOMContentLoaded", (e) => {
    const controls = document.querySelectorAll(".controls")
    for (let i=0; i < controls.length; i++) {
        let control = controls[i]
        let product_id = control.getAttribute("product-id")
        let inc = control.querySelector(".inc")
        let dec = control.querySelector(".dec")
        let count = control.querySelector(".count")
        let in_basket = control.querySelector(".in-basket")
        let in_favorites = control.querySelector(".in_favorites")
        inc.addEventListener("click", (e) => {
            count.innerHTML = parseInt(count.innerHTML) + 1
        })
        dec.addEventListener("click", (e) => {
            count.innerHTML = parseInt(count.innerHTML) - 1
            if (parseInt(count.innerHTML) === -1) {
                count.innerHTML = 0
            }
        })
        in_basket.addEventListener("click", (e) => {
            data = new FormData()
            data.append("product_id", product_id)
            data.append("count", count.innerHTML)
            axios.post("/add_product/", data)
            .then(data => {
                console.log("удачно добавлено")
                alert("Товар добавлен")
            })
            .catch(error => {
                console.log("ошибка", error)
            })
        })
        in_favorites.addEventListener("click", (e) => {
            data = new FormData()
            data.append("product_id", product_id)
            axios.post("/in_favorites/", data)
            .then(data => {
                if (data['data']['message'] === 'added') {
                    document.querySelector("#notification").innerHTML = "Товар добавлен в избранное"
                }
                if (data['data']['message'] === 'deleted') {
                    document.querySelector("#notification").innerHTML = "Товар убран из избранного"
                }
                document.querySelector("#notification").style.left = '1rem'
                setTimeout(() => {
                    document.querySelector("#notification").style.left = '-100rem'
                }, 2000);
            })
            .catch(error => {
                console.log("ошибка")
            })
        })
    }
})