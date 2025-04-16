import { Component } from "@angular/core";
import { UiButtonComponent } from "./ui-button.component";

@Component({
    selector: 'gallery-button-demo',
    standalone: true,
    imports: [UiButtonComponent],
    template: `
      <ui-button text="Submit" (clicked)="submit()"></ui-button>
    `
  })
  export class GalleryButtonDemoComponent {
    submit() {
      console.log('Submitted');
    }
  }
  