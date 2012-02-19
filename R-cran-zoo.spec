%define modulename zoo
%define realver 1.6-2
%define r_library %{_libdir}/R/library

Summary:	Z's ordered observations for R
Name:		R-cran-%{modulename}
Version:	%(echo %{realver} | tr '-' '.')
Release:	%mkrel 1
License:	GPLv2
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	R-cran-chron
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This R package provides an S3 class with methods for totally ordered 
indexed observations. It is particularly aimed at irregular time series 
of numeric vectors/matrices and factors. zoo's key design goals are 
independence of a particular index/date/time class and consistency with 
ts and base R by providing methods to extend standard generics.

%prep
%setup -q -c

%build

R CMD build --no-vignettes %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
