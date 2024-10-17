Name:		texlive-uwthesis
Version:	15878
Release:	2
Summary:	University of Washington thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uwthesis
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive uwthesis package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uwthesis/uwthesis.cls
%doc %{_texmfdistdir}/doc/latex/uwthesis/LICENSE
%doc %{_texmfdistdir}/doc/latex/uwthesis/README
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.bib
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.pdf
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
