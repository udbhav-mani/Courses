import { Component } from '@angular/core';

import { FormService } from '../app.service';
import { FormModel } from '../form-model.model';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css'],
})
export class DataComponent {
  formData: FormModel;

  constructor(private formSer: FormService) {
    this.formData = this.formSer.getForms();
  }

  ngOnInit() {
    this.formSer.newFormEvent.subscribe(() => {
      this.formData = this.formSer.getForms();
    });
  }
}
