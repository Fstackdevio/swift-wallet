import { Component, OnInit } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { ApiService } from 'src/app/api.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
regno: Number;
password: String;
  constructor(private toaster: ToastrService,private router:Router ,private Api:ApiService) { }

  ngOnInit() {
  }
  login() {
    const details = ({
      regno: this.regno,
      password: this.password
    });

    if (details.regno == null || details.password == null) {
      this.toaster.error('All Fields Are Required', 'Validation Failed');
    } else {
         this.Api.login(details).subscribe(data=>{
           if(data.StatusCode==200){
            this.toaster.success('Login Successfll', 'Login Success');
            this.router.navigate(['/dashboard'])
           }
           else{
            this.toaster.error('Incorrect Username and pasword', 'Login Failed');
           }
         })
    }

  }
}
