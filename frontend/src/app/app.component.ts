import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { CountriesApiService } from './countries/countries-api.service';
import { Country } from './countries/country.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  countriesListSubs: Subscription;
  countriesList: Country[];

  constructor(private countriesApi: CountriesApiService) {
  }

  ngOnInit() {
    this.countriesListSubs = this.countriesApi
      .getCountries()
      .subscribe(res => {
          this.countriesList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.countriesListSubs.unsubscribe();
  }
}
