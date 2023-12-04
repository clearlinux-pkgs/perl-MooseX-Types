#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-MooseX-Types
Version  : 0.50
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-0.50.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-0.50.tar.gz
Summary  : 'Organise your Moose types in libraries'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Types-license = %{version}-%{release}
Requires: perl-MooseX-Types-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Exporter)
BuildRequires : perl(Moose::Meta::TypeConstraint::Union)
BuildRequires : perl(Moose::Role)
BuildRequires : perl(Moose::Util::TypeConstraints)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Exporter::ForMethods)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution MooseX-Types,
version 0.50:
Organise your Moose types in libraries

%package dev
Summary: dev components for the perl-MooseX-Types package.
Group: Development
Provides: perl-MooseX-Types-devel = %{version}-%{release}
Requires: perl-MooseX-Types = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Types package.


%package license
Summary: license components for the perl-MooseX-Types package.
Group: Default

%description license
license components for the perl-MooseX-Types package.


%package perl
Summary: perl components for the perl-MooseX-Types package.
Group: Default
Requires: perl-MooseX-Types = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Types package.


%prep
%setup -q -n MooseX-Types-0.50
cd %{_builddir}/MooseX-Types-0.50

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Types
cp %{_builddir}/MooseX-Types-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-MooseX-Types/2c6591e5788bbef7f1f44f5810a4bb63ccf9a76c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Types.3
/usr/share/man/man3/MooseX::Types::Base.3
/usr/share/man/man3/MooseX::Types::CheckedUtilExports.3
/usr/share/man/man3/MooseX::Types::Combine.3
/usr/share/man/man3/MooseX::Types::Moose.3
/usr/share/man/man3/MooseX::Types::TypeDecorator.3
/usr/share/man/man3/MooseX::Types::UndefinedType.3
/usr/share/man/man3/MooseX::Types::Util.3
/usr/share/man/man3/MooseX::Types::Wrapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Types/2c6591e5788bbef7f1f44f5810a4bb63ccf9a76c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
