import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { Country } from './country.model';

@Injectable()
export class CountriesApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getCountries(): Observable<Country[]> {
    return this.http
      .get<Country[]>(`${API_URL}/countries`)
      .pipe(
        catchError(CountriesApiService._handleError)
      );
  }
}
