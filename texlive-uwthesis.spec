# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uwthesis
# catalog-date 2010-01-23 11:08:54 +0100
# catalog-license apache2
# catalog-version 6.13
Name:		texlive-uwthesis
Version:	6.13
Release:	4
Summary:	University of Washington thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uwthesis
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 6.13-2
+ Revision: 757335
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 6.13-1
+ Revision: 719868
- texlive-uwthesis
- texlive-uwthesis
- texlive-uwthesis

