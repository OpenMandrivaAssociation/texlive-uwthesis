# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/uwthesis
# catalog-date 2010-01-23 11:08:54 +0100
# catalog-license apache2
# catalog-version 6.13
Name:		texlive-uwthesis
Version:	6.13
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive uwthesis package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uwthesis/uwthesis.cls
%doc %{_texmfdistdir}/doc/latex/uwthesis/LICENSE
%doc %{_texmfdistdir}/doc/latex/uwthesis/README
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.bib
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.pdf
%doc %{_texmfdistdir}/doc/latex/uwthesis/uwthesis.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
