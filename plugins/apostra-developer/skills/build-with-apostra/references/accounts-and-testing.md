# Accounts, access, sandbox testing and tracking

Read this when the person asks how to structure accounts and advertisers for
their own clients, when `get_status` shows no account to work in, or before they
test or send conversion events. The product facts live in the public docs; read
the pages named here before you state one.

## Account structure

Apostra has three levels: an organization, the Buyer Accounts inside it, and the
advertisers inside a Buyer Account. The organization holds the people, the plan
and billing. It is not a place to work: campaigns, advertisers and platform
connections live in a Buyer Account.

For a builder that buys media for several clients, start with one Buyer Account
and an advertiser for each client. Give a client its own child Buyer Account only
when its own people sign in to Apostra or it needs its own billing choice with a
seller. When each client has its own ad account on a platform, connect the
platform once, then map each client's ad account to that client's advertiser. The
platform bills the client. See
[several client accounts](https://docs.apostra.com/v3/several-client-accounts)
and [how Apostra objects map to platform objects](https://docs.apostra.com/v3/concepts#how-apostra-objects-map-to-platform-objects).

A person connecting a client's ad account completes the platform's sign-in or
partner grant in a browser. Hand them the one-time URL the connection tool
returns and wait. Do not try to complete it for them.

## When `get_status` shows no account to work in

A person can work in a Buyer Account only if they hold a permission on that
account, or administer the organization that holds it. Belonging to the
organization as an Editor or Viewer is not enough: they reach the organization
and no account in it. A person in this state sees only the organization in
`get_status`, and naming a Buyer Account's `accountId` is refused with
`ACCOUNT_NOT_REACHABLE`.

Do this, in order:

1. Say what you observed: the signed-in person, the account `get_status` named,
   and that no Buyer Account is listed.
2. Tell them to ask an administrator of the Buyer Account (or of the
   organization) to add them to the Buyer Account with the Editor permission.
   Viewer is read-only, and every write is refused.
3. Stop the live work and continue the local, fixture-based work. Retry
   `get_status` after they say they were added.

Do not guess other `accountId` values or ask them to use someone else's
credentials. [Account access](https://docs.apostra.com/v3/account-access)
and [name the account on every call](https://docs.apostra.com/v3/name-the-account)
list the errors. An API key, M2M credential or buyer agent is bound to one account
and needs none of this.

## Test in the sandbox, and know where it stops

Create a sandbox advertiser with `save_advertiser` and `sandbox: true`, turn on
the Apostra synthetic seller for it, save a campaign, call `request_proposals`,
and stage a media buy. It needs no billing details and spends nothing. Read
[build end to end in the sandbox](https://docs.apostra.com/v3/developer-quickstart#build-end-to-end-in-the-sandbox)
first.

State plainly what that run proves. It proves the person's loop: discovery,
proposals and staging. It does not launch on a real ad platform or produce real
delivery, and a sandbox advertiser's buy on Meta, Google or another platform
adapter is refused. Ad platform behavior is tested with a small, capped real
campaign after the sandbox loop passes, and only when the person asks for it. A
passing sandbox run is not a successful live launch.

## Conversion events and server-side tracking

A pixel or dataset is created in the platform's own console. Apostra does not
create one. For server-side tracking, register an advertiser event source with
`save_event_source` and map it to the connected platform account, then send each
event with `log_event`. Per-event records and pre-aggregated outcomes have
different shapes, so read [bring data in](https://docs.apostra.com/v3/bring-data-in)
and retrieve the `set-up-an-event-source` skill before any write.

What an event can do depends on the platform. Read the platform's page in the
[ad platform compatibility guide](https://docs.apostra.com/v2/guides/ad-platform-compatibility/index)
for its Log Event row before promising conversion optimization on it. A platform
whose row is not Available takes no server events through Apostra yet.

## What the API does not do

Some platform features exist only in the platform's own interface. Apostra can
use only what the platform's API offers. Read
[what the API does not do](https://docs.apostra.com/v3/limitations#what-the-api-does-not-do)
before telling a builder a feature is or is not available, and send them to
[support](https://docs.apostra.com/v3/support) when it is not listed.
