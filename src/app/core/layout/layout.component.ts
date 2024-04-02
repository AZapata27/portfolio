import { Component } from '@angular/core';
import {MenuComponent} from "../../shared/menu/menu.component";
import {AboutComponent} from "../../pages/about/about.component";
import {ExperienceComponent} from "../../pages/experience/experience.component";
import {ProjectsComponent} from "../../pages/projects/projects.component";
import {ContactComponent} from "../../pages/contact/contact.component";
import {FooterComponent} from "../../shared/footer/footer.component";
import {SocialNetworksComponent} from "../../shared/social-networks/social-networks.component";

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [
    MenuComponent,
    AboutComponent,
    ExperienceComponent,
    ProjectsComponent,
    ContactComponent,
    FooterComponent,
    SocialNetworksComponent
  ],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {

}
