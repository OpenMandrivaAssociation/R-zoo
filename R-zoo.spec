%bcond_with bootstrap
%global packname  zoo
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.7_7
Release:          2
Summary:          Regular and Irregular Time Series S3 Infrastructure (Z's ordered observations)
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-7.tar.gz
Requires:         R-stats R-stats R-utils R-graphics R-grDevices R-lattice
%if %{with bootstrap}
Requires:         R-coda R-chron R-fts R-its R-lattice R-timeDate R-timeSeries
Requires:         R-tis
%else
Requires:         R-coda R-chron R-DAAG R-fts R-its R-lattice R-mondate
Requires:         R-strucchange R-timeDate R-timeSeries R-tis R-tseries R-xts
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats
BuildRequires:    R-stats R-utils R-graphics R-grDevices R-lattice
%if %{with bootstrap}
BuildRequires:    R-coda R-chron R-fts R-its R-lattice R-timeDate R-timeSeries
BuildRequires:    R-tis
%else
BuildRequires:    R-coda R-chron R-DAAG R-fts R-its R-lattice R-mondate
BuildRequires:    R-strucchange R-timeDate R-timeSeries R-tis R-tseries R-xts 
%endif
%rename R-cran-zoo

%description
An S3 class with methods for totally ordered indexed observations. It is
particularly aimed at irregular time series of numeric vectors/matrices
and factors. zoo's key design goals are independence of a particular
index/date/time class and consistency with ts and base R by providing
methods to extend standard generics.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
