var ViewModel = function() {
    this.ClickCount = ko.observable(0);
    this.name = ko.observable('Scooby');
    this.dogImg = ko.observable('img/img1.jpg');

    this.incrementCounter = function() {
        this.ClickCount(this.ClickCount() +1);
    };

    this.hasClickedTooManyTimes = ko.pureComputed(function() {
        return this.ClickCount() > 5;
    }, this);

}

ko.applyBindings(new ViewModel())
