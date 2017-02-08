// this is model object, which has all the datas
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

// octopus is a mediator between model and view.
var octopus = {

    // init function
    init: function() {
        model.currentDog = model.dogs[0];
        dogListView.init();
        dogView.init();
    },

    // this will retrieve the current dog's info from model
    getCurrentDog: function() {
        return model.currentDog;
    },

    // this will retrieve all the dogs'name
    getDogs: function() {
        return model.dogs;
    },

    // this function will set the value of currentDog
    setCurrentDog: function(dog) {
        model.currentDog = dog;
    },

    // increment of clickcount
    incrementCounter: function() {
        model.currentDog.ClickCount++;
        dogView.render();
    }
};

// this is view of dog's image and name and clickcount
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
        this.countElem.textContent = 'ClickCount is: ' + currentDog.ClickCount;
        this.dogNameElem.textContent = currentDog.name;
        this.dogImageElem.src = currentDog.dogImg;
    }
};

// this vies is of list of dogs
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
            elem.setAttribute('class', 'btn-txt btn');
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
