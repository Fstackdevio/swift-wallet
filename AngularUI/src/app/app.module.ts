import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { Routes , RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
//import { SidebarComponent } from './components/sidebar/sidebar.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { LoginComponent } from './components/login/login.component';
import { componentFactoryName } from '@angular/compiler';
import { SettingsComponent } from './components/settings/settings.component';
import { TransferComponent } from './components/transfer/transfer.component';
const approutes:Routes = [
{path:'',pathMatch:'full',redirectTo:'login'},
{path:"dashboard",component:DashboardComponent},
{path:'login',component:LoginComponent},
{path:'settings',component:SettingsComponent},
{path:'transfer',component:TransferComponent}
]
@NgModule({
  declarations: [
    AppComponent,
   
    DashboardComponent,
    LoginComponent,
    TransferComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(approutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }