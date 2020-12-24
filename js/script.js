/*alert("Bienvenidos a mi página");

let correo=prompt("Ingrese su correo para recibir notificaciones:"); //  funcion prompt lee por pantalla un texto
console.log("Su correo es:"+correo);*/

new Vue({
    el: '#app',

    data(){
        return {
            name: "Bitcoin",
            img:'https://i.pinimg.com/originals/6f/3f/6f/6f3f6f671839f72561c6e8686a8ebcbc.jpg',
            changePercent:0,
            prices: [8400, 7900, 8200, 9000, 9400, 10000, 10200],
            pricesWithDays: [
                { day: 'Lunes', value: 8400 },
                { day: 'Martes', value: 7900 },
                { day: 'Miercoles', value: 8200 },
                { day: 'Jueves', value: 9000 },
                { day: 'Viernes', value: 9400 },
                { day: 'Sabado', value: 10000 },
                { day: 'Domingo', value: 10200 },
            ],
            showPrices: false

        }
        
    },
    methods: {
        toggleShowPrices(){
            this.showPrices = !this.showPrices
        }
    }

})