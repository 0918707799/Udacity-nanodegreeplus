var model = {
    currentDog: null,
    dogs: [
        {
            ClickCount: 0,
            name: 'Scooby',
            dogImg: 'img/img1.jpg'
        },
        {
            ClickCount: 0,
            name: 'Popoye',
            dogImg: 'img/img2.jpg'
        },
        {
            ClickCount: 0,
            name: 'Tom',
            dogImg: 'img/img3.jpg'
        },
        {
            ClickCount: 0,
            name: 'Ruffy',
            dogImg: 'img/img4.jpg'
        },
        {
            ClickCount: 0,
            name: 'Blue',
            dogImg: 'img/img5.jpg'
        },
        {
            ClickCount: 0,
            name: 'Augie',
            dogImg: 'img/img6.jpg'
        },
        {
            ClickCount: 0,
            name: 'Bruno',
            dogImg: 'img/img7.jpg'
        }
    ]
};

var octopus = {

    init: function() {
        model.currentDog = model.dogs[0];
        dogListView.init();
        dogView.init();
    },

    getCurrentDog: function() {
        return model.currentDog;
    },

    getDogs: function() {
        return model.dogs;
    },

    setCurrentDog: function(dog) {
        model.currentDog = dog;
    },

    incrementCounter: function() {
        model.currentDog.ClickCount++;
        dogView.render();
    }
};

var dogView = {
    init: function() {
        this.dogElem = document.getElementById('dog');
        this.dogNameElem = document.getElementById('dog-name');
        this.dogImageElem = document.getElementById('dog-img');
        this.countElem = document.getElementById('dog-count');

        this.dogImageElem.addEventListener('click', function(){
            octopus.incrementCounter();
        });

        this.render();
    },

    render: function() {
        var currentDog = octopus.getCurrentDog();
        this.countElem.textContent = currentDog.ClickCount;
        this.dogNameElem.textContent = currentDog.name;
        this.dogImageElem.src = currentDog.dogImg;
    }
};

var dogListView = {

    init: function() {
        this.dogListElem = document.getElementById('dog-list');
        this.render();
    },

    render: function() {
        var dog, elem, i;

        var dogs = octopus.getDogs();

        this.dogListElem.innerHTML = '';

        for (i=0; i < dogs.length; i++) {
            dog = dogs[i];

            elem = document.createElement('li');
            elem.textContent = dog.name;

            elem.addEventListener('click', (function(dogCopy) {
                return function() {
                    octopus.setCurrentDog(dogCopy);
                    dogView.render();
                };
            })(dog));

            this.dogListElem.appendChild(elem);

        }
    }
};

octopus.init();
