%global tl_name uwthesis
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.13
Release:	%{tl_revision}.1
Summary:	University of Washington thesis class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uwthesis
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
University of Washington thesis class

