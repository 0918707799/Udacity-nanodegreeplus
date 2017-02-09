var Dog = function(data) {
    this.ClickCount = ko.observable(data.ClickCount);
    this.name = ko.observable(data.name);
    this.dogImg = ko.observable(data.dogImg);
    this.nickname = ko.observableArray(data.nickname);
    this.buffer = ko.observable("doggie");


    this.bufferfunction = ko.computed(function() {
        if (this.ClickCount() > 20) {
            return this.buffer('People like this dog');
        } else if (this.ClickCount() > 10){
            return this.buffer('People are crazy for this dog');
        } else {
            return this.buffer('doggie');
        }
    }, this);
}

var initialDogs = [
    {
            ClickCount: 0,
            name: 'Scooby',
            dogImg: 'img/img1.jpg',
            nickname: ['Superman', 'Spiderman']
        },
        {
            ClickCount: 0,
            name: 'Popoye',
            dogImg: 'img/img2.jpg',
            nickname: ['Flash', 'Aquaman']
        },
        {
            ClickCount: 0,
            name: 'Tom',
            dogImg: 'img/img3.jpg',
            nickname: ['Iron-man']
        },
        {
            ClickCount: 0,
            name: 'Ruffy',
            dogImg: 'img/img4.jpg',
            nickname: ['Thor']
        },
        {
            ClickCount: 0,
            name: 'Blue',
            dogImg: 'img/img5.jpg',
            nickname: ['Batman']
        },
        {
            ClickCount: 0,
            name: 'Augie',
            dogImg: 'img/img6.jpg',
            nickname: ['captain']
        },
        {
            ClickCount: 0,
            name: 'Bruno',
            dogImg: 'img/img7.jpg'
        }
]

var ViewModel = function() {
    var self = this;

    this.dogList = ko.observableArray([]);

    initialDogs.forEach(function(dogItem){
        self.dogList.push(new Dog(dogItem));
    });

    this.currentDog = ko.observable( this.dogList()[0] );

    this.incrementCounter = function() {
        self.currentDog().ClickCount(self.currentDog().ClickCount() +1);
    };

};

ko.applyBindings(new ViewModel());
