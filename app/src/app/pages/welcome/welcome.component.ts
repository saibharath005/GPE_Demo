import { Component } from '@angular/core'
import { Title, Meta } from '@angular/platform-browser'

@Component({
  selector: 'app-welcome',
  templateUrl: 'welcome.component.html',
  styleUrls: ['welcome.component.css'],
})
export class Welcome {
  constructor(private title: Title, private meta: Meta) {
    this.title.setTitle('Massive Rich Dinosaur')
    this.meta.addTags([
      {
        property: 'og:title',
        content: 'Massive Rich Dinosaur',
      },
    ])
  }
}
