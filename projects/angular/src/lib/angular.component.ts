import { Component } from '@angular/core';
import { ButtonComponent } from './button/button.component'; 
import { TextBoxComponent} from './text-box/text-box.component'; // adjust import based on your build
import { PasswordBoxComponent } from './password-box/password-box.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'lib-angular',
  imports: [],
  template: `
    <p>
      angular works!
    </p>
  `,
  styles: ``
})
export class AngularComponent {

}
