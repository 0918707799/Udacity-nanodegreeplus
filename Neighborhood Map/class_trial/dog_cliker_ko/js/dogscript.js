var Dog = function() {
    this.ClickCount = ko.observable(0);
    this.name = ko.observable('Scooby');
    this.dogImg = ko.observable('img/img1.jpg');
    this.nickname = ko.observableArray(['Superman', 'Spiderman', 'Batman'])
    this.buffer = ko.observable('dog');


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

var ViewModel = function() {
    this.currentDog = ko.observable( new Dog() );

    this.incrementCounter = function() {
        this.ClickCount(this.ClickCount() +1);
    };

};

ko.applyBindings(new ViewModel());
