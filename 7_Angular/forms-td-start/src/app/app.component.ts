import { Component, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('f') signupForm: NgForm;
  suggestUserName() {
    const suggestedName = 'Superuser';
  }
  onSubmit() {
    console.log(this.signupForm);
  }

  genders = ['male', 'female'];

  newArray = this.myFilter(this.genders, (gender) => {
    return gender === 'male';
  });

  myFilter(genders, func) {
    const newGendersArray = [];
    for (let gender of genders) {
      if (func(gender)) {
        newGendersArray.push(gender);
      }
    }
    return newGendersArray;
  }
}
