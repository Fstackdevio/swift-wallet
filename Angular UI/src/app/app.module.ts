import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import{Routes,RouterModule} from '@angular/router';
import { DashboarComponent } from './components/dashboar/dashboar.component';
import { SettingsComponent } from './components/settings/settings.component'

const app : Routes = [
  {path:'',pathMatch:'full',redirectTo:'dashboard'},
  {path:'dashboard',component:DashboarComponent},
  {path:'settings',component:SettingsComponent}
]
@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    DashboarComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(app)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
