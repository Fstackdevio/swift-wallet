import { Injectable } from '@angular/core';
import {Http, Headers} from '@angular/http';
import "rxjs/add/operator/map"
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: Http) { }
  login(details) {
      let headers = new Headers;
      headers.append('Content-Type', 'application/json');
      return this.http.post('http://127.0.0.1:5000/Authenticate',details)
      .map(res=>res.json())
  } 
}
