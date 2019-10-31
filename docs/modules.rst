.. _api-documentation:

==================
API Documentation
==================

Cards
-----

.. autoclass:: pyadaptivecards.card.AdaptiveCard
    :members:
    :inherited-members:

    .. automethod:: __init__

Components
----------

This section covers all the different components that can be added to the body of a adaptive card. 

.. autoclass:: pyadaptivecards.components.Image()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.components.TextBlock()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.components.Column()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.components.Fact()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.components.Choice()
   :members:

   .. automethod:: __init__

Options
-------

Options allow you to configure the look and behaviour of components and containers. 

.. autoclass:: pyadaptivecards.options.VerticalContentAlignment()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.Colors()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.HorizontalAlignment()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.FontSize()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.FontWeight()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.BlockElementHeight()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.Spacing()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.ImageSize()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.ImageStyle()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.ContainerStyle()
   :members:
   :undoc-members

.. autoclass:: pyadaptivecards.options.TextInputStyle()
   :members:
   :undoc-members:

.. autoclass:: pyadaptivecards.options.ChoiceInputStyle()
   :members:
   :undoc-members:


Container
---------

.. autoclass:: pyadaptivecards.container.Container()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.container.ColumnSet()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.container.FactSet()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.container.ImageSet()
   :members:

   .. automethod:: __init__

Inputs
------

.. autoclass:: pyadaptivecards.inputs.Text()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.inputs.Number()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.inputs.Date()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.inputs.Time()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.inputs.Toggle()
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.inputs.Choices()
   :members:

   .. automethod:: __init__

Actions
-------

.. autoclass:: pyadaptivecards.actions.OpenUrl
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.actions.Submit
   :members:

   .. automethod:: __init__

.. autoclass:: pyadaptivecards.actions.ShowCard
   :members:

   .. automethod:: __init__
