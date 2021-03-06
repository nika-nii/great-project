var app = new Vue({
    el: '#app',
    data() {
        return {
            posts: [
                { 
                    title: 'День учителя в 2021',
                    category: 'Школьные будни',
                    text: 'День учителя — один из самых известных, любимых и широко отмечаемых профессиональных праздников. Поэтому весь лицей готовился к нему, одни готовили праздничный концерт для учителей, другие занимались распределением ролей на День дублера, третьи - украшением здания.' 
                },
                {
                    title: 'Межрегиональная олимпиада по праву "Фемида"',
                    category: 'Объявления',
                    text: 'День учителя — один из самых известных, любимых и широко отмечаемых профессиональных праздников. Поэтому весь лицей готовился к нему, одни готовили праздничный концерт для учителей, другие занимались распределением ролей на День дублера, третьи - украшением здания.'
                }
            ]
        };
    },
    mounted() {
        axios
            .get('http://127.0.0.1:8000/news/')
            .then(response => {
                this.posts = response.data 
                console.log(response.data)
                });
    }
});


