import { Component, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

import { FormModel, ReimbursementModel } from '../form-model.model';
import { FormService } from '../app.service';

@Component({
  selector: 'app-form',
  templateUrl: './form-component.component.html',
  styleUrls: ['./form-component.component.css'],
})
export class FormComponent {
  @ViewChild('formData') formData: NgForm | undefined;
  inputForms: FormModel;
  constructor(private formSer: FormService) {}

  ngOnInit() {
    this.inputForms = this.formSer.inputForms;
  }

  onAdd() {
    this.inputForms.reimbursement.push(new ReimbursementModel('', null, ''));
    this.formSer.inputForms = this.inputForms;
  }
  onSubmit() {
    this.formSer.newFormEvent.next(true);
  }
  onDelete(index: number) {
    this.inputForms.reimbursement.splice(index, 1);
  }
}
