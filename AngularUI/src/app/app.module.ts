import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { Routes , RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
//import { SidebarComponent } from './components/sidebar/sidebar.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { LoginComponent } from './components/login/login.component';
import { componentFactoryName } from '@angular/compiler';
import { SettingsComponent } from './components/settings/settings.component';
import { TransferComponent } from './components/transfer/transfer.component';
import { SupportComponent } from './components/support/support.component';
import { TransactionsComponent } from './components/transactions/transactions.component';
import {FormsModule} from "@angular/forms"
import { ToastrModule } from 'ngx-toastr';
import { HttpModule } from '@angular/http';
const approutes:Routes = [
{path:'',pathMatch:'full',redirectTo:'login'},
{path:"dashboard",component:DashboardComponent},
{path:'login',component:LoginComponent},
{path:'settings',component:SettingsComponent},
{path:'transfer',component:TransferComponent},
{path:'support',component:SupportComponent},
{path:'transactions',component:TransactionsComponent}
]
@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    LoginComponent,
    TransferComponent,
    SettingsComponent,
    SupportComponent,
    TransactionsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(approutes),
    ToastrModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
